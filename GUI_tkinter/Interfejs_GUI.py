import tkinter as tk


class Aplication(tk.Frame):
	def __init__(self,master):
		super(Aplication,self).__init__(master)
		self.grid()
		self.button_clicks = 0
		self.kolumna = 1
		self.create_widgets()
	def create_widgets(self):
		self.button = tk.Button(self)
		self.button["text"] = "liczba klikniec : 0 "
		self.button["command"] = self.klikniecie
		self.button.grid()
	def klikniecie(self):
		self.button_clicks += 1
		self.button["text"]= "liczba klikniec : " + str(self.button_clicks)
"""
# UTWORZENIE OKNA APLIKACJI
root = tk.Tk()
root.title("OKNO GLOWNE")
root.geometry("400x400")
root.resizable(0,1)

# ZAPYTANIA DO NAUKI 
#print(help(tk.Tk()))
#print(dir("root"))
#print(help("tkinter"))
#print(help(tk.Label()))


#TWORZENIE ELEMENTOW
# utworz w oknie jako pojemnik na elementy
app = tk.Frame(root)
app.grid()
lbl=tk.Label(app,text="JESTEM ETYKIETA",background = "#ff0000",activeforeground="#ff0000")
lbl.grid()
butt=tk.Button(app,text="przycisk")
butt.grid()



root.mainloop()
"""
def command():
	print("TAKTOPANIE")
	app.button["background"]="#ff0000"
	app.button["text"]="TAKTOPANIE"
	app.button["padx"]=10
	app.button["pady"]=10
	app.button["activebackground"]="#00ff00"

root = tk.Tk()
root.title("okno główne")
root.geometry("400x300")
root.bbox(row = 4, column = 4)
app = Aplication(root)
app2 = Aplication(root)

app.button["command"] = command
app.grid(row=0,column = 0,rowspan = 2)
app2.grid(row=2,column=0,rowspan = 1)
root.mainloop()
