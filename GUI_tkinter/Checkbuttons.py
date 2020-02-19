# program checkbutton
import tkinter as tk


class Aplication(tk.Frame):
	def __init__(self,master):
		super(Aplication,self).__init__(master)
		self.grid()
		self.create_Widgets()
		
	def create_Widgets(self):
		#utworz etykiete
		tk.Label(self,text = " Wybierz swoje ulubione gatunki filmow.").grid(row = 0, column = 0, sticky = 'w')
		#utworz etykiete
		tk.Label(self,text = " Zaznacz wszystkie, które chciałbyś wybrać:").grid(row = 1, column = 0, sticky = 'w')
		#utworz checkbutton komedia
		self.likes_comedy = tk.BooleanVar()
		self.likes_dramat = tk.BooleanVar()
		self.likes_horror = tk.BooleanVar()
		
		tk.Checkbutton(self, text = "komedia", variable = self.likes_comedy, command = self.update_text).grid(row = 3, column = 0, sticky ='w')
		tk.Checkbutton(self, text = "dramat", variable = self.likes_dramat, command = self.update_text).grid(row = 4, column = 0, sticky ='w')
		tk.Checkbutton(self, text = "horror", variable = self.likes_horror, command = self.update_text).grid(row = 5, column = 0, sticky ='w')
		#utworzenie okna wynikow 
		self.result = tk.Text(self)
		self.result.grid(row =6,column=0,sticky='w')
	def update_text(self):
		likes = ""
		if self.likes_comedy.get():
			likes += "Lubisz filmy komediowe.\n"
		if self.likes_dramat.get():
			likes += "Lubisz filmy dramatyczne.\n"
		if self.likes_horror.get():
			likes += "Lubisz horrory.\n"
			
		self.result.delete(0.0, 'end')
		self.result.insert(0.0,likes)
		
		
okno = tk.Tk()
okno.title("okno glowne")
okno.geometry("300x300")
okno.minsize(100,100)


obiekt = Aplication(okno)

okno.mainloop()

