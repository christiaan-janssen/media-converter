# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Mar  3 06:46:01 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(661, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.statusText = QtGui.QLabel(self.centralwidget)
        self.statusText.setGeometry(QtCore.QRect(20, 90, 271, 17))
        self.statusText.setObjectName(_fromUtf8("statusText"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 230, 641, 192))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.selectFileButton = QtGui.QPushButton(self.centralwidget)
        self.selectFileButton.setGeometry(QtCore.QRect(10, 20, 141, 61))
        self.selectFileButton.setObjectName(_fromUtf8("selectfileButton"))
        self.convertButton = QtGui.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(160, 20, 141, 61))
        self.convertButton.setObjectName(_fromUtf8("convertButton"))
        self.androidHDRaioButton = QtGui.QRadioButton(self.centralwidget)
        self.androidHDRaioButton.setGeometry(QtCore.QRect(390, 70, 201, 22))
        self.androidHDRaioButton.setChecked(True)
        self.androidHDRaioButton.setObjectName(_fromUtf8("androidHDRaioButton"))
        self.androidQHDRaioButton = QtGui.QRadioButton(self.centralwidget)
        self.androidQHDRaioButton.setGeometry(QtCore.QRect(390, 100, 116, 22))
        self.androidQHDRaioButton.setObjectName(_fromUtf8("androidQHDRaioButton"))
        self.appleHDRadioButton = QtGui.QRadioButton(self.centralwidget)
        self.appleHDRadioButton.setGeometry(QtCore.QRect(390, 130, 116, 22))
        self.appleHDRadioButton.setObjectName(_fromUtf8("appleHDRadioButton"))
        self.appleFullHDRadioButton = QtGui.QRadioButton(self.centralwidget)
        self.appleFullHDRadioButton.setGeometry(QtCore.QRect(390, 160, 116, 22))
        self.appleFullHDRadioButton.setObjectName(_fromUtf8("appleFullHDRadioButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.statusText.setText(_translate("MainWindow", "TextLabel", None))
        self.selectFileButton.setText(_translate("MainWindow", "Select Media File", None))
        self.convertButton.setText(_translate("MainWindow", "Convert", None))
        self.androidHDRaioButton.setText(_translate("MainWindow", "Android HD", None))
        self.androidQHDRaioButton.setText(_translate("MainWindow", "Android qHD", None))
        self.appleHDRadioButton.setText(_translate("MainWindow", "Apple HD", None))
        self.appleFullHDRadioButton.setText(_translate("MainWindow", "Apple Full HD", None))

