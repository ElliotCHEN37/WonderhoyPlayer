import sys
import io
import threading
import json
import requests
import webbrowser
from PyQt5 import QtWidgets, QtGui, QtCore
from main_win import Ui_MainWindow
from pydub import AudioSegment
from pydub.playback import play


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, config):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/ico/wonderhoy.ico'))

        self._setup_ui_elements()
        self.mode = int(config.get("mode", 0))
        self.audio_thread = None
        self.stop_audio_flag = threading.Event()

        self.actionCheck_for_update.triggered.connect(self.check_for_updates)

    def _setup_ui_elements(self):
        wdh = QtGui.QPixmap(':/img/wonderhoy.png').scaled(296, 256)
        self.img.setIcon(QtGui.QIcon(wdh))
        self.img.setIconSize(wdh.size())
        self.img.clicked.connect(self.play_audio)

        swp = QtGui.QPixmap(':/img/swap.png').scaled(100, 100)
        self.mode_button.setIcon(QtGui.QIcon(swp))
        self.mode_button.clicked.connect(self.toggle_mode)

        self.actionExit.triggered.connect(self.close)
        self.actionAbout.triggered.connect(self.show_about_dialog)
        self.spd.currentIndexChanged.connect(self.change_speed)

    def toggle_mode(self):
        self.mode = 1 if self.mode == 0 else 0
        self.setWindowTitle(self.tr(f"Wonderhoy Player! - {'Infinite' if self.mode else 'Regular'} mode"))
        if self.audio_thread and self.audio_thread.is_alive():
            self.stop_audio_flag.set()
            self.audio_thread.join()
            self.play_audio()

    def change_speed(self):
        self.stop_audio()
        self.play_audio()

    def play_audio(self):
        if self.audio_thread and self.audio_thread.is_alive():
            self.stop_audio_flag.set()
            self.audio_thread.join()

        self.stop_audio_flag.clear()

        def play_wav():
            audio_file = QtCore.QFile(':/snd/wonderhoy.wav')
            if audio_file.open(QtCore.QFile.ReadOnly):
                audio_data = audio_file.readAll()
                audio_file.close()
                audio = AudioSegment.from_file(io.BytesIO(audio_data), format="wav")

                speed_text = self.spd.currentText()
                try:
                    playback_speed = float(speed_text.replace('x', ''))
                    if playback_speed == 1.0:
                        # Play without speed adjustment
                        while not self.stop_audio_flag.is_set():
                            play(audio)
                            if self.mode == 0:
                                break
                    else:
                        # Adjust playback speed
                        audio = audio.speedup(playback_speed=playback_speed)
                        while not self.stop_audio_flag.is_set():
                            play(audio)
                            if self.mode == 0:
                                break

                except ValueError:
                    print(f"Invalid speed option: {speed_text}")

        self.audio_thread = threading.Thread(target=play_wav)
        self.audio_thread.start()

    def stop_audio(self):
        self.stop_audio_flag.set()
        if self.audio_thread:
            self.audio_thread.join()

    def show_about_dialog(self):
        QtWidgets.QMessageBox.about(self, self.tr("About"),
                                    self.tr("Wonderhoy Player v1.2 by ElliotCHEN37\nLicensed under MIT License\n"
                                            "Build time: 24/07/01"))

    def check_for_updates(self):
        def fetch_remote_build():
            try:
                response = requests.get('https://raw.githubusercontent.com/ElliotCHEN37/WonderhoyPlayer/main/cfu.json')
                if response.status_code == 200:
                    remote_config = response.json()
                    remote_build = int(remote_config.get("build", 0))
                    local_build = 3
                    if remote_build > local_build:
                        QtCore.QMetaObject.invokeMethod(self, "prompt_update", QtCore.Qt.QueuedConnection)
                    else:
                        QtCore.QMetaObject.invokeMethod(self, "prompt_no_update", QtCore.Qt.QueuedConnection)
            except Exception as e:
                print(f"Failed to fetch remote build: {e}")

        threading.Thread(target=fetch_remote_build).start()

    @QtCore.pyqtSlot()
    def prompt_update(self):
        reply = QtWidgets.QMessageBox.question(self, self.tr("A new update is available"),
                                               self.tr(
                                                   "A new version of Wonderhoy Player is available! Do you want to update now?"),
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            webbrowser.open("https://github.com/ElliotCHEN37/WonderhoyPlayer/releases/latest")

    @QtCore.pyqtSlot()
    def prompt_no_update(self):
        QtWidgets.QMessageBox.information(self, self.tr("No update available"),
                                          self.tr("You are using the latest version"))

    def closeEvent(self, event):
        self.stop_audio()
        event.accept()


if __name__ == "__main__":
    with open('config.json', 'r') as f:
        config = json.load(f)

    app = QtWidgets.QApplication(sys.argv)

    trans_file = config.get("trans", "")
    if trans_file:
        trans = QtCore.QTranslator()
        trans.load(trans_file)
        app.installTranslator(trans)

    window = MainWindow(config)
    window.show()
    window.retranslateUi(window)
    sys.exit(app.exec_())
