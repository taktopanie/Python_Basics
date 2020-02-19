from PyQt5 import QtCore, QtGui, QtWidgets
import ComboBox as CB
import sys

class Combobox(CB.Ui_MainWindow):
	def setupUi(self,master):
		super(Combobox,self).setupUi(master)
		
		self.pushButton.clicked.connect(self.funkcja_przycisku)
		
	def funkcja_przycisku(self):
		tekst = self.comboBox.currentText()
		if(tekst == "1Hz"):
			self.textBrowser.setText("TAKTO")
		else:
			self.textBrowser.setText(tekst)


def main():
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Combobox()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

main()
