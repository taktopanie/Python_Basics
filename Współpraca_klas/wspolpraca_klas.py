
class Pierwsza_klasa(object):
	def __init__(self,nazwa):
		self.__nazwa = nazwa
		print("utworzono obiekt klasy o nazwie : ", self.__nazwa)
	def metoda(self):
		print("metoda")
		
	@property
	def name(self):
		return self.__nazwa
	@name.setter
	def name(self,nazwa):
		if(nazwa != "LOL"):
			self.__nazwa = nazwa
			print("zmieniona nazwa to : ", self.__nazwa)
		else:
			print("nie udalo sie zmienic nazwy, nazwa to : ", self.__nazwa)
	@name.getter
	def name(self):
		print("zadzialal getter")
		
		
		
class Druga_klasa(Pierwsza_klasa):
	def __init__(self,nazwa):
		super(Druga_klasa,self).__init__(nazwa)
		print("dodatkowo dopisany tekst w konstruktorze klasy drugiej")
	def metoda(self):
		super(Druga_klasa,self).metoda()
		print("metoda drugiej klasy a nie pierwszej")
		
obiekt = Pierwsza_klasa("pierwszy_obiekt") 
print("nazwa pobrana z funkcji glownej to : ", obiekt.name)
obiekt.name = "LOL2"
obiekt2= Druga_klasa("pierwszy obiekt drugiej klasy")
obiekt2.metoda()
