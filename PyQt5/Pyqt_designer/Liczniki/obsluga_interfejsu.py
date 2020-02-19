#obsługa modułu 

import Main 
import sys


from PyQt5 import QtCore, QtGui, QtWidgets

class Modul(Main.Ui_MainWindow):
	def setupUi(self,nazwa):
		super(Modul, self).setupUi(nazwa);
		self.ustawienia_poczatkowe()
		self.licznik1=0
		self.licznik2=0
		self.stan=0
		
	def ustawienia_poczatkowe(self):
		self.pushButton.clicked.connect(self.wcisniecie_przycisku)
		
	def wcisniecie_przycisku(self):
		print("Przycisk wcisniety")
		if self.stan == 0:
			timer1.start(100)
			timer2.start(200)
			self.stan = 1
		elif self.stan == 1:
			timer1.stop()
			timer2.stop()
			self.stan=0
		self.lcdNumber.display(self.licznik1)
		self.lcdNumber_2.display(self.licznik2)
	def funkcja_timer1(self):
		self.licznik1 +=1
		self.lcdNumber.display(self.licznik1)
	def funkcja_timer2(self):
		self.licznik2 +=1
		self.lcdNumber_2.display(self.licznik2)


app = QtWidgets.QApplication(sys.argv)



MainWindow = QtWidgets.QMainWindow()
ui = Modul()
ui.setupUi(MainWindow)
MainWindow.show()

timer1 = QtCore.QTimer()
timer1.timeout.connect(ui.funkcja_timer1)


timer2 = QtCore.QTimer()
timer2.timeout.connect(ui.funkcja_timer2)

sys.exit(app.exec_())
