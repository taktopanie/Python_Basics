import sys

class Bank(object):
	__saldo =0
	
	def __init__(self):
		print("Utworzono nowe konto bankowe !\n")
	
	def wplata(self):
		ilosc_p = input("ile pieniedzy chcesz wplacic : ")
		print("czy jestes pewnien ze chcesz wplacic : ",ilosc_p," zlotych? (t/n)")
		if(input().upper()=='T'):
			Bank.__saldo +=int(ilosc_p)
			print("wplacono ", ilosc_p, "zlotych.\n")
		else:
			print("nie rozpoznano decyzji\n")
	def wyplata(self):
		print("wyplata")
		ilosc_p = int(input("ile pieniedzy chcesz wyplacic : "))
		if((Bank.__saldo - ilosc_p) <0):
			print("\nbrak wystarczajacych srodkow na koncie, sprobuj inna kwote\n")
		else:
			Bank.__saldo = Bank.__saldo - ilosc_p
			print("srodki zostaly wyplacone\n")
	
	def sprawdzenie_salda(self):
		print("Obecne saldo na koncie wynosi : ", Bank.__saldo," zl.\n")
		

def main():
	
	print("""
			MENU GLOWNE
	1. wplata
	2. wyplata
	3. sprawdzenie salda
		
	""")
	decyzja = input()
	if(decyzja == '1'):
		try:
			konto.wplata()
		except:
			print("nie moge wplacic pieniedzy, konto prawdopodobnie nie istnieje")
	elif(decyzja == '2'):
		konto.wyplata()
	elif(decyzja == '3'):
		konto.sprawdzenie_salda()	
	
if(input("Program banku, aby przejsc do menu glownego nacisnik enter, aby wyjsc nacisnik q ")== 'q'):
	sys.exit()
log_new_q = input("Aby utworzyc nowe konto nacisnij N, aby zalogowac L ").upper()
if(log_new_q == 'N'):
	konto = Bank()
elif(log_new_q == 'L'):
	print ("logowanie")
while(1):
	
	main()
