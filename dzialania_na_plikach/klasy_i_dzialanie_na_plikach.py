#klasy_i_pliki
import sys

class Plik(object):
	## atrybut klasy
	ilosc_plikow = 0
	##konstruktor klasy
	def __init__(self,name):
		self.name = name +".txt"
		Plik.ilosc_plikow +=1
		try:
			plik = open(self.name,'w')
		except:
			print("\nnie udalo sie utworzyc pliku o nazwie :", self.name)
			print("\n\n") 
		else:	
			print("utworzono nowy plik o nazwie :",self.name, "\n\n")
			plik.close()
			
	## metoda klasy
	def zapisywanie(self):
		plik = open(self.name,"w")
		plik.write(input("co zapisac do pliku :"))
		plik.close()		
	def odczytywanie(self):
		plik = open(self.name,"r")
		print("zawartosc pliku to : ", plik.read(), "\n")
		plik.close()
	def koniec(self):
		print("koniec programu")
		sys.exit()
		
	@staticmethod
	def status():
		print("ilosc plikow to : ",Plik.ilosc_plikow,".\n")
			
			
def sprawdzenie_i_utw_pliku():
	nazwa_pliku = input("Podaj nazwę pliku jaki mam utworzyć: """)
	print("\n\n")
	try:
		open(nazwa_pliku+".txt",'r')
	except:
		plik = Plik(nazwa_pliku)
	else:
		decyzja_istnienia = (input("Plik juz istnieje czy go nadpisac ? T/N : "))
		if(decyzja_istnienia.upper()=='T' ):
			plik = Plik(nazwa_pliku)
		else:
			print(" akcja anulowana \n")
			plik = sprawdzenie_i_utw_pliku()
	return plik
			
	

			

plik = sprawdzenie_i_utw_pliku()
while(1):
	decyzja = input("Aby zapisac dane do pliku nacisnij : Z, aby odczytac : O, aby zakonczyc nacisnij Q aby utworzyc nowy plik nacisnij N : ")
	print("\n")
	## metoda zakonczenia
	if(decyzja == 'q' or decyzja == 'Q'):
		Plik.status()
		plik.koniec()
	## metoda zapisu
	elif(decyzja == 'z' or decyzja == 'Z'):
		plik.zapisywanie()
	## metoda odczytywania 
	elif(decyzja == 'o' or decyzja == 'O'):
		plik.odczytywanie()
	##metoda utworzenia nowego pliku
	elif(decyzja == 'n' or decyzja == 'N'):
		sprawdzenie_i_utw_pliku()
	
