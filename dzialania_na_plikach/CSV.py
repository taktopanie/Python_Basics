# plik skanujacy plik csv 

import csv 

path = "/home/macko/Pobrane/5c90b26e8f798b4bf2b34ef6d36c358a.csv"

lines =[line for line in open(path)]

print(lines[1])


