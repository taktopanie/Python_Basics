# pyQt5 program 

from PyQt5.QtWidgets import (QWidget, QSlider, 
    QLabel, QApplication,QPushButton, QMessageBox,QVBoxLayout,QHBoxLayout)
from PyQt5.QtGui import QPixmap
import sys

"""

class Kalkulator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        self.resize(300, 100)
        self.setWindowTitle("Prosty kalkulator")
        self.setWindowIconText("LOL")
        self.show()

"""
def funkcja_klawisza():
	QApplication.beep()
	QApplication.widgetAt(200,300)
	print("klawisz został wciśnięty")
	print(QApplication.applicationDisplayName())

#utworzenie okna
app = QApplication(sys.argv)
okno1 = QWidget()
okno1.resize(400, 100)
okno1.setWindowTitle("OKNO GŁÓWNE")

#utworzenie widgetow
label = QLabel("Patrz na mnie")
przycisk = QPushButton("Nacisnij mnie")

#utworzenie siatki
#HORYZONTALNA
h_box = QHBoxLayout()
h_box.addStretch()
h_box.addWidget(label)
h_box.addStretch()

#PIONOWA
v_box = QVBoxLayout()
v_box.addLayout(h_box)
v_box.addWidget(przycisk)

okno1.setLayout(v_box)

przycisk.clicked.connect(funkcja_klawisza)
#wlaczenie okna
okno1.show()
sys.exit(app.exec_())
   
