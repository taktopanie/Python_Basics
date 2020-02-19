import sys 
import time 


""" #####################LISTA

def utworzenie_listy():
	wartosc = ''
	while(wartosc != "q"):
		wartosc = input("podaj wartosci jakie chcesz zapisac w liscie lub ""q"" aby zakonczyc : ")
		lista.append(wartosc)
lista=[]
def main():		
	utworzenie_listy()	
	return(lista)

print(main())

"""
"""
################# SLOWNIK
def utworzenie_slownika():
	slownik.update({"takto" : 5, "kurwa" : "mac"})
	
slownik = dict()

def main():
	 utworzenie_slownika()
	 return slownik["kurwa"]
	 
print(main())
"""

############## KROTKA

def utworzenie_krotki():
	krotka = ("PIERWSZY", "LOL", "taktopanie")
	return krotka
	
def main():
	utworzona_krotka = utworzenie_krotki()
	try : utworzona_krotka[1] = "zmienione"
	except: 
		print("nie udalo sie zmienic wartosci krotki.\n")
	else : 
		print("wartosc krotki zmieniona.\n ")
		
	krotka_druga = (utworzona_krotka[1],"zmienione",*utworzona_krotka[0:2])
	print(krotka_druga)
	print(krotka_druga[2])
main()
