#test
import tkinter as tk

class Aplikacja (tk.Frame):
	def __init__(self,master):
		super(Aplikacja,self).__init__(master)
		self.grid()
		self.Createwidgets()
		self.contents = "0"
		
	def Createwidgets(self):
		self.inst_lbl = tk.Label(self,text="Podaj nawzę pliku jaki mam utworzyć")
		self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = 'W')
		#utworzenie etykiety do nazwy pliku
		self.pw_lbl = tk.Label(self, text="Nazwa pliku: ")
		self.pw_lbl.grid(row = 2, column = 0, sticky = 'W')
		self.pw_lbl = tk.Label(self, text=" ")
		self.pw_lbl.grid(row = 1, column = 0, sticky = 'W')
		#utworz widget Entry
		self.pw_ent = tk.Entry(self)
		self.pw_ent.grid(row = 2, column = 1, sticky = 'W')
		#utworz przycisk akceptuj 
		self.sumbit_bttn = tk.Button(self, text="Akceptuj",command = self.utworzenie_pliku)
		self.sumbit_bttn.grid(row=3, column=0, sticky='W')
		#utworzenie przycisku wyczysc
		self.wyczysc_bttn = tk.Button(self, text="Wyczysc okno",command = self.czyszczenie_konsoli)
		self.wyczysc_bttn.grid(row=3, column=1, sticky='W')
		
		#tworze widget Text do zapisu wiadomosci
		self.secret_txt=tk.Text(self, width = 35, height = 5, wrap = "word")
		self.secret_txt.grid(row = 4, column = 0, columnspan = 2, sticky = 'W')
		#utworzenie przycisku zapis 
		self.butt_zapis = tk.Button(self,text="zapis",command=self.zapis, borderwidth = 10, background = "#237053")
		self.butt_zapis.grid(padx = 50,row = 5, column = 0, columnspan = 2)
		
	#metoda sprawdzajaca czy istnieje dany plik
	def utworzenie_pliku(self):
		self.contents = self.pw_ent.get()
		self.contents +=".txt"
		
		try: plik = open(self.contents, 'r')
		except:
			self.tworzenie_plikow()
		else:
			self.secret_txt.insert(1.0,"Plik juz istnieje czy ma zostać nadpisany :\n Akceptuj = tak, Wyczysc okno = nie ?")
			self.sumbit_bttn.configure(command = self.zgoda)
			self.wyczysc_bttn.configure(command = self.niezgoda)
		
		
	#metoda zapisujaca tekst do pliku
	def zapis(self):
		wiadomosc =self.secret_txt.get(1.0,'end' )
		try :self.plik.write(str(wiadomosc))
		except:
			print("NIE pobrano i zapisano tekst : " + wiadomosc)
		else:
			print("pobrano i zapisano tekst : " + wiadomosc)
			self.czyszczenie_konsoli()
			self.secret_txt.insert(1.0,"Zapisano podany tekst, aby dopisać powtórz procedurę zapisu, aby stworzyć nowy plik wprowadź nową nazwę")
	#metoda czyszczaca okno konsoli
	def czyszczenie_konsoli(self):
		self.secret_txt.delete(1.0 , "end")
	#metoda wykonywana po zgodzie na nadpisanie pliku
	def zgoda(self):
		self.powrot_funkcji()
		try: self.plik = open(self.contents, 'w')
		except:
			self.czyszczenie_konsoli()
			self.secret_txt.insert(1.0,"nie udalo sie utworzyc pliku : " + self.contents + "\n")
		else:
			self.czyszczenie_konsoli()
			self.secret_txt.insert(1.0,"plik : " + self.contents + " zostal nadpisany. Wyczyść konsolę i wprowadź tekst jaki chcesz zapisać.\n")
	#metoda wykonywana po niezgodzie na nadpisanie pliku
	def niezgoda(self):
		self.powrot_funkcji()
		self.czyszczenie_konsoli()
		self.secret_txt.insert(1.0,"nie udalo sie utworzyc pliku ")
	#metoda przywracajaca przyciskom stare funkcje
	def powrot_funkcji(self):
		self.wyczysc_bttn.configure(command = self.czyszczenie_konsoli)
		self.sumbit_bttn.configure(command = self.utworzenie_pliku)
	#utworzenie pliku
	def tworzenie_plikow(self):
		try: self.plik = open(self.contents, 'w')
		except:
			self.czyszczenie_konsoli()
			self.secret_txt.insert(1.0,"nie udalo sie utworzyc pliku : " + self.contents + "\n")
		else:
			self.czyszczenie_konsoli()
			self.secret_txt.insert(1.0,"utworzono plik : " + self.contents + ", Wyczyść konsolę i wprowadź tekst jaki chcesz zapisać.\n")
		
root = tk.Tk()
root.title("okno glowne")
root.geometry("300x300")
przycisk = Aplikacja(root)
root.mainloop()
