#plik zapisuje dane binarne do plików dat
import pickle

try:
	plik = open("plik_bin.dat","wb")
except:
	print("nie ma takiego pliku.\n")
else:
	print("plik otworzony\n")
	
	
lista_pierwsza = ["pierwszy_obiekt","drugi_obiekt","trzeci_obiekt"]

lista_druga = ["pierwszy_obiektl2","drugi_obiektl2","trzeci_obiektl2"]

pickle.dump(lista_pierwsza,plik)
pickle.dump(lista_druga,plik)
plik.close()

zmienna1 = []
zmienna2 = []
plik = open("plik_bin.dat","rb")
for obiekt in pickle.load(plik):
	zmienna1.append(obiekt)
	
for obiekt in pickle.load(plik):
	zmienna2.append(obiekt)
plik.close();


print("zawartosc pierwszej pobranej listy to : ", zmienna1, "\n")
print("zawartosc drugiej pobranej listy to : ", zmienna2, "\n")

remove(zmienna[1])
