#Klikanie diody 

import serial
from PyQt5 import QtWidgets, QtSerialPort
import sys

class Aplikacja(QtWidgets.QWidget):
	def __init__(self):
		super(Aplikacja,self).__init__()
		self.setGeometry(2,2,200,200)
		self.tworzenie_widgetow()
		self.funkcja_klawisza2()
		self.stan=0
		
	def tworzenie_widgetow(self):
		#utworzenie Labela
		label1 = QtWidgets.QLabel()
		label1.setText("ABY ZAPALIC DIODE NACISNIJ PRZYCISK")
		label1.setMaximumSize(300,100)

		
		#utworzenie Przycisku1
		self.button1 = QtWidgets.QPushButton(self)
		self.button1.setText("DIODA ON")
		self.button1.clicked.connect(self.funkcja_klawisza1)
		self.button1.setMinimumSize(100,100)
		self.button1.setStyleSheet("background-color: rgb(0,255,0)")
		self.button1.setToolTip('Taktopanie')
		
		#utworzenie Przycisku2
		self.button2 = QtWidgets.QPushButton()
		self.button2.setText("DIODA OFF")
		self.button2.clicked.connect(self.funkcja_klawisza2)
		self.button2.setMinimumSize(100,100)
		self.button2.setStyleSheet("background-color: red")
		
		#stworzenie siatki
		v_box = QtWidgets.QVBoxLayout()
		h1_box = QtWidgets.QHBoxLayout()
		h2_box = QtWidgets.QHBoxLayout()
		
		h1_box.addStretch()
		h1_box.addWidget(label1)
		h1_box.addStretch()
		
		h2_box.addWidget(self.button1)
		h2_box.addStretch()
		h2_box.addWidget(self.button2)
		
		v_box.addLayout(h1_box)
		v_box.addLayout(h2_box)
		
		#h_box.addStretch()
		#h_box.addWidget(label1)
		#h_box.addStretch()
		#v_box.addLayout(h_box)

		#v_box.addWidget(self.button1)

		#v_box.addWidget(self.button2)

		self.move(600,200)
		self.setMinimumWidth(400)
		self.setMinimumHeight(500)
		self.setLayout(v_box)
		self.show() 
	


	def funkcja_klawisza1(self):
		print("DIODA ON")
		self.button2.setEnabled(1)
		self.button1.setEnabled(0)
		#otwarcie portu i wyslanie danych
		SERIAL = serial.Serial('/dev/ttyUSB0')
		SERIAL.write(b'#01*21+')
		SERIAL.close()
	
	def funkcja_klawisza2(self):
		print("DIODA OFF")
		self.button2.setEnabled(0)
		self.button1.setEnabled(1)
		#otwarcie portu i wyslanie danych
		SERIAL = serial.Serial('/dev/ttyUSB0')
		SERIAL.write(b'#01*20+')
		SERIAL.close()

#class Menu(object):
#	def __init__(self):


app = QtWidgets.QApplication(sys.argv)
widget = Aplikacja()


"""
w = QtWidgets.QWidget()
w.setGeometry(2,2,200,200)

#utworzenie Labela
label1 = QtWidgets.QLabel()
label1.setText("ABY ZAPALIC DIODE NACISNIJ PRZYCISK")
label1.setMaximumSize(300,100)

#utworzenie Przycisku1
button1 = QtWidgets.QPushButton()
button1.setText("DIODA ON")
button1.clicked.connect(funkcja_klawisza1)
button1.setMinimumSize(200,100)

#utworzenie Przycisku2
button2 = QtWidgets.QPushButton()
button2.setText("DIODA OFF")
button2.clicked.connect(funkcja_klawisza2)
button2.setMinimumSize(200,100)

#stworzenie siatki
v_box = QtWidgets.QVBoxLayout()
h_box = QtWidgets.QHBoxLayout()

h_box.addStretch()
h_box.addWidget(label1)
h_box.addStretch()
v_box.addLayout(h_box)

v_box.addWidget(button1)

v_box.addWidget(button2)

w.move(600,200)
w.setMinimumWidth(300)
w.setMinimumHeight(500)
w.setLayout(v_box)
w.show() 

"""


sys.exit(app.exec())
