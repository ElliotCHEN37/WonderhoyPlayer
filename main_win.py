# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(10, 41, 618, 57))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.welcome_label.setFont(font)
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")
        self.img = QtWidgets.QPushButton(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(150, 110, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(50)
        self.img.setFont(font)
        self.img.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.img.setStyleSheet("QPushButton\n"
"{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}")
        self.img.setText("")
        self.img.setObjectName("img")
        self.mode_button = QtWidgets.QPushButton(self.centralwidget)
        self.mode_button.setGeometry(QtCore.QRect(500, 210, 100, 100))
        self.mode_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mode_button.setStyleSheet("QPushButton\n"
"{\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}")
        self.mode_button.setText("")
        self.mode_button.setIconSize(QtCore.QSize(100, 100))
        self.mode_button.setObjectName("mode_button")
        self.spd = QtWidgets.QComboBox(self.centralwidget)
        self.spd.setGeometry(QtCore.QRect(29, 220, 91, 22))
        self.spd.setObjectName("spd")
        self.spd.addItem("")
        self.spd.addItem("")
        self.spd.addItem("")
        self.spd.addItem("")
        self.spd.addItem("")
        self.spd.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 190, 101, 21))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCheck_for_update = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_update.setObjectName("actionCheck_for_update")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionCheck_for_update)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wonderhoy Player!"))
        self.welcome_label.setText(_translate("MainWindow", "Wonderhoy! Click the sticker to play wonderhoy!\n"
"You can change the playing mode by clicking the \'swap\' button!"))
        self.spd.setPlaceholderText(_translate("MainWindow", "Speed"))
        self.spd.setItemText(0, _translate("MainWindow", "1x"))
        self.spd.setItemText(1, _translate("MainWindow", "2x"))
        self.spd.setItemText(2, _translate("MainWindow", "5x"))
        self.spd.setItemText(3, _translate("MainWindow", "10x"))
        self.spd.setItemText(4, _translate("MainWindow", "100x"))
        self.spd.setItemText(5, _translate("MainWindow", "1000x"))
        self.label.setText(_translate("MainWindow", "Playback speed"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionCheck_for_update.setText(_translate("MainWindow", "Check for update"))
import resources_rc
