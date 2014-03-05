#!/usr/bin/env python3
from PyQt4 import QtCore, QtGui
from os.path import expanduser
import os
import shlex
import sys # Importand to get the sys.argv to work on my installation

__author__ = 'Christiaan Janssen'

# Import converted Python UI file
from mainwindow import Ui_MainWindow

class Main(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		# Connect the buttons:
		QtCore.QObject.connect(self.ui.selectFileButton,QtCore.SIGNAL("clicked()"),self.selectFile)
		QtCore.QObject.connect(self.ui.convertButton,QtCore.SIGNAL("clicked()"),self.convert)

		# Connect the radio buttons:
		QtCore.QObject.connect(self.ui.androidHDRadioButton,QtCore.SIGNAL("toggled(bool)"),self.androidHDSelected)
		QtCore.QObject.connect(self.ui.androidQHDRadioButton,QtCore.SIGNAL("toggled(bool)"),self.androidQHDSelected)
		QtCore.QObject.connect(self.ui.appleHDRadioButton,QtCore.SIGNAL("toggled(bool)"),self.appleHDSelected)
		QtCore.QObject.connect(self.ui.appleFullHDRadioButton,QtCore.SIGNAL("toggled(bool)"),self.appleFullHDSelected)

	def selectFile(self):
		fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open Media File', expanduser('~'),'Media Files(*.mov *.avi *.mkv *.mpg)')
		self.ui.fileName.setText(fileName)

	def convert(self):
		self.convertFile()

	def androidHDSelected(self):
		self.ui.outputFormat.setText("Android HD")

	def androidQHDSelected(self):
		self.ui.outputFormat.setText("Android QHD")

	def appleHDSelected(self):
		self.ui.outputFormat.setText("Apple HD")

	def appleFullHDSelected(self):
		self.ui.outputFormat.setText("Apple Full HD")

def main():
	app = QtGui.QApplication(sys.argv)
	window = Main()
	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()


