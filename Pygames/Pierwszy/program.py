#pygames
from livewires import games, color
import random

class Mysz(games.Sprite):
	"""Duch sterowany myszą"""
	
	def update(self):
		self.x = games.mouse.x
		self.y = 400
		
		self.check_collide()
	def check_collide(self):
		"""sprawdz czy nie doszlo do kolizji"""
		for element in self.overlapping_sprites:
			duszek.przerwanie()
#			while(element in self.overlapping_sprites):
#				print("takto")
			
#klasa duszka 
class Duszek(games.Sprite):
	"""piłka lająca"""
	def __init__(self, image, angle=0,
                 x=0, y=0,
                 top=None, bottom=None, left=None, right=None,
                 dx=0, dy=0,
                 interval=1, is_collideable=True):
		super(Duszek,self).__init__(image, angle, x, y, top, bottom, left, right, dx, dy, interval, is_collideable)
		#dane do wyniku i poziomu trudnosci
		self.wynik = 0
		self.poziom = 1
                 
	#nadpisanie metody update
	def update(self):
		if self.right >= games.screen.width or self.left <= 0:
			self.dx = -self.dx
		if self.bottom >= games.screen.height or self.top <= 0:
			self.dy = -self.dy
		self.utrudnienie()
	
	def przerwanie(self):
		#self.x = random.randint(70,games.screen.width-70)
		#self.y = random.randint(70,120)
		self.dy = -self.dy
		self.wynik +=1
		text.set_value("Odbite piłki : " + str(self.wynik))
		text2.set_value("Poziom : " + str(self.poziom))
		
	def utrudnienie(self):
		if self.wynik ==5:
			self.poziom = 2
			self.zwiekszenie_predkosci()
		elif self.wynik == 10:
			#self.zwiekszenie_predkosci()
			self.poziom = 3
		elif self.wynik == 15:
		#	self.zwiekszenie_predkosci()
			self.poziom = 4
		
	def zwiekszenie_predkosci(self):
		if self.dx >0 and self.dy>0:
			self.dx+=1
			self.dy+=1
		elif self.dx>0 and self.dy<0:
			self.dx+=1
			self.dy-=1
		elif self.dx<0 and self.dy<0:
			self.dx-=1
			self.dy-=1
		elif self.dx<0 and self.dy>0:
			self.dx-=1
			self.dy+=1
#utworzenie okna
okno = games.init(screen_width= 640,screen_height = 480, fps = 50)
wall_image = games.load_image("tło.bmp",transparent = False)
games.screen.background = wall_image
#utworzenie duszka piłki
obraz_pilka = games.load_image("PIŁKA.bmp", transparent = True)
duszek = Duszek(image = obraz_pilka,x = games.screen.get_width()/2 ,y = games.screen.get_height()/2, dx=1, dy = 1)
#utworzenie tekstu
text = games.Text(x=150,y=30,value = "Odbite piłki : 0",color=color.dark_green ,size=50)
text2 = games.Text(x=400,y=30,value = "Poziom : 1",color=color.dark_green ,size=50)
#utworzenie powiadomienia 
message = games.Message(value = "DZIEŃ DOBRY KURWA", size = 70, x = games.screen.get_width()/2 \
,y = games.screen.get_height()/2, color = color.pink, lifetime =500)
# utworzenia kursora 
obraz_Mysz = games.load_image("pizza.bmp", transparent = False)
mysz = Mysz(image = obraz_Mysz)

#dodanie do okna widgetow
games.screen.add(mysz)
games.screen.add(duszek)
games.screen.add(text)
games.screen.add(text2)
games.screen.add(message)

#kursor nie moze opuscic okna 
games.screen.set_event_grab(True)

#kursor niewidoczny 
games.mouse.set_is_visible(False)

#petla glowna okna
games.screen.mainloop()
