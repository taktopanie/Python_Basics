
class Klasa_testowa(object):
	def __init__(self):
		print("utworzono nowy obiekt klasy :"+ str(self) +"\n")
#	def __init__(self, nazwa):
#		print("utworzono nowy obiekt klasy :"+ str(self) +"i podano argument : "  + nazwa + "\n")
	def __str__(self):
		return("Klasa_testowa")
		
	def metoda_pierwsza(self):
		print("metoda pierwsza \n")
	def metoda_pierwsza(self, zmienna):
		print("metoda pierwsza lecz przeladowana zmienna : " + zmienna + "\n")
		
obiekt = Klasa_testowa()
obiekt.metoda_pierwsza()
