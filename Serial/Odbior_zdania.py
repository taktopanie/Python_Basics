# Odbieranie danych z UART do testow

import serial
import time 
import Lista_portow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets





def funkcja_timer():
	print("taktopanie")




porty = Lista_portow.funkcja_zwrotu_portow()
print("dostepne porty szeregowe to : ")
i=1
for port in porty:
	print(str(i) + ". " + str(port) +"\n")
	i+=1
numer_portu = input("Podaj numer portu z ktorym chcesz sie polaczyc : ")
if numer_portu == 'q':
	sys.exit()
	
numer_portu=(int(numer_portu)-1)
	
while(1):
	
	try: SERIAL = serial.Serial(port = porty[numer_portu],baudrate=9600,timeout = 1)
	except:
		print("Pomiar nie dziala, sprawdz port.")
		break
	else:
		komenda = (input("Podaj komende jaka mam wyslac na port : "))
		
		
		SERIAL.write(str.encode(komenda+'+'))
		
		timer = QtCore.QTimer()
		timer.timeout.connect(funkcja_timer)
		timer.start(500)
		
		time.sleep(2)
		print(SERIAL.in_waiting)
		zdanie = SERIAL.read(100).decode('utf-8')
		print(SERIAL.in_waiting)
		print(zdanie)
		SERIAL.close()
