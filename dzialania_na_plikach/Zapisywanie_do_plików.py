## program ma za zadanie przetestowanie dzialania na plikach

import time 
import pickle

czas = time.time()
zmienna_czas = time.localtime(czas)

godziny = zmienna_czas.tm_hour
minuty = zmienna_czas.tm_min
sekundy = zmienna_czas.tm_sec

plik = open("plik_tekstowy.txt","w")
plik.write("GODZINA : ")
plik.write(str(godziny))
plik.write(":")
plik.write(str(minuty))
plik.write(":")
plik.write(str(sekundy))
plik.close()
plik = open("plik_tekstowy.txt","r")
print ("GODZINA : ", godziny,":",minuty,":", sekundy,"\n")
print (plik.readline())
print (plik.readline(3))
print (plik.readline())
print (plik.readline(3))

plik.close()
