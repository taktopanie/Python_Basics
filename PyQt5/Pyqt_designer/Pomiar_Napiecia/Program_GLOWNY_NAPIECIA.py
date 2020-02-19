# PROGRAM GLOWNY

import GUI
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import serial

class Dodane_funkcje(GUI.Ui_Okno_Glowne):
	def setupUi(self, Okno_Glowne):
		super(Dodane_funkcje, self).setupUi(Okno_Glowne)
		#self.lcdNumber.setDecMode
		self.lcdNumber.display("0.00 ")
		self.ustawienie_widgetow()
	
	def ustawienie_widgetow(self):
		self.SERIAL = serial.Serial('/dev/ttyUSB0',baudrate=9600)
		
		self.pushButton.clicked.connect(self.pomiar)
		#self.pushButton.clicked.connect(self.textEdit.paste)
	def pomiar(self):
		self.SERIAL.write(b'#02*11+')
		zdanie = self.SERIAL.readline().decode('utf-8')
		if zdanie == '\n':
			zdanie = self.SERIAL.readline().decode('utf-8')
		#zdanie += ch
		print(zdanie)
		self.lcdNumber.display(zdanie)
"""
app = QtWidgets.QApplication(sys.argv)
Okno_Glowne = QtWidgets.QWidget()
ui = Dodane_funkcje()
ui.setupUi(Okno_Glowne)
Okno_Glowne.show()
sys.exit(app.exec_())
"""

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Dodane_funkcje()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
    
    
    
