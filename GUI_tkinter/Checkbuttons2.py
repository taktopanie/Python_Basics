#checkbuttons_2
import tkinter as tk

class Aplikacja(tk.Frame):
	def __init__(self,master):
		super(Aplikacja,self).__init__(master)
		self.grid()
		self.utworzenie_widgetow()
		
	def utworzenie_widgetow(self):
		tk.Label(self,text = "Wybierz gatunek filmu jaki lublisz.").grid(row = 0, column = 0,padx=15)
		self.zmienna_do_przechowywania = tk.StringVar()
		self.zmienna_do_przechowywania.set(None)
		#przycisk 1
		tk.Radiobutton(self,text = "Komedia", value = "Komediowy", command = self.update_text, variable = self.zmienna_do_przechowywania).grid(row=1,column=0)
		#przycisk 2
		tk.Radiobutton(self,text = "Dramat", value = "Dramatyczny", command = self.update_text, variable = self.zmienna_do_przechowywania).grid(row=2,column=0)
		#przycisk 3
		tk.Radiobutton(self,text = "taktopanie", value = "taktopanie", command = self.update_text, variable = self.zmienna_do_przechowywania).grid(row=3,column=0)
		#okno tekstowe
		self.tekst = tk.Text(self,width=25,height = 6,wrap = "word")
		self.tekst.grid(row=4,column=0)	
		#Checkbutton 1 
		self.zmienna_do_opcja1 = tk.BooleanVar()
		tk.Checkbutton(self,text = "opcja 1", command = self.update_text, variable = self.zmienna_do_opcja1).grid(row = 5,column = 0)
		#Checkbutton 2 
		self.zmienna_do_opcja2 = tk.BooleanVar()
		tk.Checkbutton(self,text = "opcja 2", command = self.update_text, variable = self.zmienna_do_opcja2).grid(row = 6,column = 0)
		#Checkbutton 3 
		self.zmienna_do_opcja3 = tk.BooleanVar()
		tk.Checkbutton(self,text = "opcja 3", command = self.update_text, variable = self.zmienna_do_opcja3).grid(row = 7,column = 0)
	def update_text(self):
		self.tekst.delete(0.0,'end')
		self.tekst_do_wysw = ""
		if self.zmienna_do_przechowywania.get() != "None":
			self.tekst_do_wysw = "Lubisz filmy, które mają gatunek :\n" + self.zmienna_do_przechowywania.get()
		#opcja 1
		if self.zmienna_do_opcja1.get():
			self.tekst_do_wysw += "\nopcja 1"
		#opcja 2
		if self.zmienna_do_opcja2.get():
			self.tekst_do_wysw += "\nopcja 2"
		#opcja 3
		if self.zmienna_do_opcja3.get():
			self.tekst_do_wysw += "\nopcja 3"
		self.tekst.insert(0.0,self.tekst_do_wysw)
		
root = tk.Tk()
root.title("Okno główne")
root.geometry("300x300")

app = Aplikacja(root)

root.mainloop()

