# program ma na celu wykorzystanie klas i integracji z uzytkownikiem|| Podstawy menu || 

import random as rand

class Liczby(object):
	def __init__(self,name):
		self.name = name
		self.low = 0
		self.high = 2
		print("utworzono obiekt o nazwie : ",self.name,".\n")
	def __str__(self):
		print("odpowiedz na zapytanie o obiekt : ")
		return(self.name)
	def ask_no_yes(self,question):
		decyzja = 0
		while decyzja not in ("t","n"):
			decyzja = input(question).lower()
		return decyzja
	def wybor_liczby(self,LOW,HIGH):
		liczba_wylosowana = -1
		while liczba_wylosowana not in range (LOW,HIGH):
			liczba_wylosowana = rand.randint(0,100)
		return liczba_wylosowana
		
		
		
		
		
obiekt_klasy = Liczby("pierwszy")
print("zapytanie o obiekt : ", obiekt_klasy)

"""
decyzja = obiekt_klasy.ask_no_yes("ZAPYTANIE ??\n")
if decyzja == "t":
	print("dobrze panie!!")
elif decyzja == "n":
	print("niedobrze")
"""
decyzja_menu = 0
while(decyzja_menu != "q"):
	
	decyzja_menu = input("""
			MENU GLOWNE 
		1. wybor liczby
		2. zapytanie
		q - aby wyjsc
		
		DECYZJA : """)
	if decyzja_menu == '1':
		try: low = int(input("podaj dolny zakres z którego mam wylosowac liczbe : "))
		except:
			print("nie podano liczby !!")
			continue
		try: high = int(input("podaj gorny zakres z którego mam wylosowac liczbe : "))
		except:
			print("nie podano liczby !!")
			continue
			
		if high<low:
			print("bledny zakres\n")
			continue
		obiekt_klasy.low = low
		obiekt_klasy.high = (high+1)
		print("liczba wylosowana z przedzialu od ", obiekt_klasy.low , " do ", obiekt_klasy.high-1, " to : ", str(obiekt_klasy.wybor_liczby(obiekt_klasy.low,obiekt_klasy.high)))


	elif decyzja_menu == '2':
		decyzja = obiekt_klasy.ask_no_yes("ZAPYTANIE ??\n")
		if decyzja == "t":
			print("dobrze panie!!")
		elif decyzja == "n":
			print("niedobrze")
