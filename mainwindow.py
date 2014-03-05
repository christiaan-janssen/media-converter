# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Mar  5 19:56:00 2014
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
        MainWindow.resize(659, 480)
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
        self.selectFileButton.setObjectName(_fromUtf8("selectFileButton"))
        self.convertButton = QtGui.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(160, 20, 141, 61))
        self.convertButton.setObjectName(_fromUtf8("convertButton"))
        self.androidHDRadioButton = QtGui.QRadioButton(self.centralwidget)
        self.androidHDRadioButton.setGeometry(QtCore.QRect(390, 70, 201, 22))
        self.androidHDRadioButton.setChecked(True)
        self.androidHDRadioButton.setObjectName(_fromUtf8("androidHDRadioButton"))
        self.androidQHDRadioButton = QtGui.QRadioButton(self.centralwidget)
        self.androidQHDRadioButton.setGeometry(QtCore.QRect(390, 100, 116, 22))
        self.androidQHDRadioButton.setObjectName(_fromUtf8("androidQHDRadioButton"))
        self.appleHDRadioButton = QtGui.QRadioButton(self.centralwidget)
        self.appleHDRadioButton.setGeometry(QtCore.QRect(390, 130, 116, 22))
        self.appleHDRadioButton.setObjectName(_fromUtf8("appleHDRadioButton"))
        self.appleFullHDRadioButton = QtGui.QRadioButton(self.centralwidget)
        self.appleFullHDRadioButton.setGeometry(QtCore.QRect(390, 160, 116, 22))
        self.appleFullHDRadioButton.setObjectName(_fromUtf8("appleFullHDRadioButton"))
        self.outputFormat = QtGui.QLabel(self.centralwidget)
        self.outputFormat.setGeometry(QtCore.QRect(20, 140, 281, 17))
        self.outputFormat.setObjectName(_fromUtf8("outputFormat"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.statusText.setText(_translate("MainWindow", "Ready to roll!", None))
        self.selectFileButton.setText(_translate("MainWindow", "Select Media File", None))
        self.convertButton.setText(_translate("MainWindow", "Convert", None))
        self.androidHDRadioButton.setText(_translate("MainWindow", "Android HD", None))
        self.androidQHDRadioButton.setText(_translate("MainWindow", "Android qHD", None))
        self.appleHDRadioButton.setText(_translate("MainWindow", "Apple HD", None))
        self.appleFullHDRadioButton.setText(_translate("MainWindow", "Apple Full HD", None))
        self.outputFormat.setText(_translate("MainWindow", "Android HD", None))

