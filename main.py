import sys
import io
import threading
import json
import PyQt5 as qt
from main_win import Ui_MainWindow
from pydub import AudioSegment
from pydub.playback import play


class MainWindow(qt.QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, config):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(qt.QtGui.QIcon(':/ico/wonderhoy.ico'))

        wdh = qt.QtGui.QPixmap(':/img/wonderhoy.png').scaled(296, 256)
        self.img.setIcon(qt.QtGui.QIcon(wdh))
        self.img.setIconSize(wdh.size())
        self.img.clicked.connect(self.play_audio)

        swp = qt.QtGui.QPixmap(':/img/swap.png').scaled(100, 100)
        self.mode_button.setIcon(qt.QtGui.QIcon(swp))
        self.mode_button.clicked.connect(self.toggle_mode)

        self.actionExit.triggered.connect(self.close)
        self.actionAbout.triggered.connect(self.show_about_dialog)

        self.mode = int(config.get("mode", 0))
        self.audio_thread = None
        self.stop_audio_flag = threading.Event()

        if self.mode == 1:
            self.setWindowTitle(self.tr("Wonderhoy Player! - Infinite mode"))
        else:
            self.setWindowTitle(self.tr("Wonderhoy Player! - Regular mode"))

    def toggle_mode(self):
        if self.mode == 0:
            self.mode = 1
            self.setWindowTitle(self.tr("Wonderhoy Player! - Infinite mode"))
        else:
            self.mode = 0
            self.setWindowTitle(self.tr("Wonderhoy Player! - Regular mode"))

        self.stop_audio()

    def play_audio(self):
        if self.audio_thread is not None and self.audio_thread.is_alive():
            self.stop_audio_flag.set()
            self.audio_thread.join()

        self.stop_audio_flag.clear()

        def play_wav():
            audio_file = qt.QtCore.QFile(':/snd/wonderhoy.wav')
            if audio_file.open(qt.QtCore.QFile.ReadOnly):
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
        qt.QtWidgets.QMessageBox.about(self, self.tr("About"),
                                       self.tr("Wonderhoy Player v1.1 by ElliotCHEN37\nLicensed under MIT License\n"
                                               "Build time: 24/06/27"))

    def closeEvent(self, event):
        self.stop_audio()
        event.accept()


if __name__ == "__main__":
    with open('config.json', 'r') as f:
        config = json.load(f)

    app = qt.QtWidgets.QApplication(sys.argv)

    trans_file = config.get("trans", "")
    if trans_file:
        trans = qt.QtCore.QTranslator()
        trans.load(trans_file)
        app.installTranslator(trans)

    window = MainWindow(config)
    window.show()
    window.retranslateUi(window)
    sys.exit(app.exec_())
