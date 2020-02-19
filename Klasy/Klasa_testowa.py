#ABY ZROBIC OGRANICZENIE CO DO ZMIANY NAZWY OBIEKTU KLASY MUSZE WYKORZYSTAC WLASCIWOSCI
#I ZMIENIC ZMIENNO NAME NA PRYWATNA CZYLI __NAME

class Klasa_testowa(object):
	atrybut = 2
	def __init__(self,name):
		
		self.__name = name
	def metoda_publiczna(self):
		print("wartosc atrybutu to : ", Klasa_testowa.atrybut, " a nazwa obiektu to", self.name, "\n")
	def __metoda_prywatna(self):
		print(" zawartosc metody prywatnej.\n")
		
	@property
	def name (self):
		return self.__name
	@name.setter
	def name(self, nowa_nazwa):
		if(nowa_nazwa == "LOL"):
			print("nie moge nazwy zmienic na : ", nowa_nazwa)
		else:
			print("nie moge zmienic nazwy, plik tylko do odczytu.\n")
			#self.__name= nowa_nazwa
		
		
		
obiekt = Klasa_testowa("obiekt_pierwszy")
obiekt.metoda_publiczna()
print(" wyswietlam nazwe obiektu w petli glownje : ", obiekt.name, "\n")
obiekt.name="taktopa"
print(" wyswietlam nazwe obiektu po zmianie w petli glownje : ", obiekt.name, "\n")

