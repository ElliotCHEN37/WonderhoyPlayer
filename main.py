import sys
import io
import threading
from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from main_win import Ui_MainWindow
from pydub import AudioSegment
from pydub.playback import play


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon(':/ico/wonderhoy.ico'))

        wdh = QPixmap(':/img/wonderhoy.png').scaled(296, 256)
        self.img.setIcon(QIcon(wdh))
        self.img.setIconSize(wdh.size())
        self.img.clicked.connect(self.play_audio)

        swp = QPixmap(':/img/swap.png').scaled(100, 100)
        self.mode.setIcon(QIcon(swp))
        self.mode.clicked.connect(self.toggle_mode)

        self.actionExit.triggered.connect(self.close)
        self.actionAbout.triggered.connect(self.show_about_dialog)

        self.mode = 0
        self.audio_thread = None
        self.stop_audio_flag = threading.Event()

    def toggle_mode(self):

        if self.mode == 0:
            self.mode = 1
            self.setWindowTitle("Wonderhoy Player! - Infinite mode")
        else:
            self.mode = 0
            self.setWindowTitle("Wonderhoy Player! - Regular mode")

        self.stop_audio()

    def play_audio(self):
        if self.audio_thread is not None and self.audio_thread.is_alive():
            self.stop_audio_flag.set()
            self.audio_thread.join()

        self.stop_audio_flag.clear()

        def play_wav():
            audio_file = QFile(':/snd/wonderhoy.wav')
            if audio_file.open(QFile.ReadOnly):
                audio_data = audio_file.readAll()
                audio_file.close()
                audio = AudioSegment.from_file(io.BytesIO(audio_data), format="wav")
                while not self.stop_audio_flag.is_set():
                    play(audio)
                    if self.mode == 0:
                        break

        self.audio_thread = threading.Thread(target=play_wav)
        self.audio_thread.start()

    def stop_audio(self):
        self.stop_audio_flag.set()
        if self.audio_thread is not None:
            self.audio_thread.join()

    def show_about_dialog(self):
        QtWidgets.QMessageBox.about(self, "About",
                                    "Wonderhoy Player v1.0 by ElliotCHEN37\nLicensed under MIT License\n"
                                    "Build time: 06/26/24")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
