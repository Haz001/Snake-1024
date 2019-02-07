try:
	import pygame
	pygame.init()
except:
	print("----<error>-----\nSomething wrong with pygame\nPlz run with Python 3 and make sure pygame is installed")
	input()
	exit()
a = False
b = False
c = False
try:
	import random
	a = True
	import time
	b = True
	import threading
	c = True
	import os
	d = True
except:
	print("----<error>-----\nProblem with imported modules\nModules\t\t|Imported\t|\n----------------|---------------|\nrandom\t\t|"+str(a)+"\t\t|\ntime\t\t|"+str(b)+"\t\t|\nthreading\t|"+str(c)+"\t\t|\nos\t\t|"+str(d)+"\t\t|\nPlease fix")
def strtobool(s):
  return s.lower() in ("true", "yes", "1")
class var:
	class grid:
		width = 16
		height = 16
		blockwidth = 32
		color1 = (32,32,32)
		color2 = (64,64,64)
	class screen:
		width = 16
		height = 16
		full = False
	class rules:
		wallloop = False
	class misc:
		modes= []
		font = pygame.font.SysFont('Consolas', 15)
		coloroffset = 4
		scene = 0
	class current:
		mode = 2
		highscore = 0
		points = 0
		deaths = 0
		state = 0
	class py:
		tick = 100
		clock = pygame.time.Clock()
		screen = pygame.display.set_mode((100, 100))
	def getvar(num):
		file = open("snake.data",'r')
		tmp = (file.read())
		tmp = tmp.split("\n")
		tmp = tmp[num].split(";")
		for i in range(len(tmp)):
			if(len(tmp[i].split(":"))== 2):
				if(tmp[i].split(":")[0].lower() == "bombs"):
					var.bomb.enabled = strtobool(tmp[i].split(":")[1])
					print(str(var.bomb.enabled)+" = "+str(strtobool(tmp[i].split(":")[1])))
				elif(tmp[i].split(":")[0].lower() == "walls"):
					var.rules.wallloop = not(strtobool(tmp[i].split(":")[1]))
				elif(tmp[i].split(":")[0].lower() == "speed"):
					var.snake.speed = float(tmp[i].split(":")[1])
				elif(tmp[i].split(":")[0].lower() == "accel"):
					var.snake.accel = float(tmp[i].split(":")[1])
				elif(tmp[i].split(":")[0].lower() == "lengt"):
					var.snake.length = float(tmp[i].split(":")[1])
		file.close()

	def modes():
		file = open("snake.data",'r')
		tmp = (file.read())
		tmp = tmp.split("\n")
		for num in range(len(tmp)):
			var.misc.modes.append(tmp[num].split(";")[0])
		file.close()
	class apple:
		color = (0,255,0)
		x = 0
		y = 0
		lvl = 0
		def place():
			var.apple.x = random.randint(1,var.grid.width-2)
			var.apple.y = random.randint(1,var.grid.height-2)
			# while not(check(var.apple.x, var.apple.y)):
			#	 var.apple.x = random.randint(1,var.grid.width-2)
			#	 var.apple.y = random.randint(1,var.grid.height-2)
	class bomb:
		enabled = True
		color = (0,255,0)
		x = 0
		y = 0
		lvl = 0
		def place():
			var.bomb.x = random.randint(1,var.grid.width-2)
			var.bomb.y = random.randint(1,var.grid.height-2)
			while (4>((var.bomb.x-var.apple.x)**2+(var.bomb.y-var.apple.y)**2)**0.5):
				 var.bomb.x = random.randint(1,var.grid.width-2)
				 var.bomb.y = random.randint(1,var.grid.height-2)
	class snake:
		color = (0,0,192)
		length = 4
		x = 0
		y = 0
		direction = 5
		lastdir = 5
		speed = float(5)
		accel = float(0.5)
		deaths = 0
		class tail:
			x = []
			y = []


	def setup():
		if(os.path.isfile("hs.data")):
			try:
				file = open("hs.data",'r')
				var.current.highscore = int(file.read())
				file.close()
			except:
				var.current.highscore = 0
		else:
			var.current.highscore = 0
		var.screen.width = var.grid.width*var.grid.blockwidth
		var.screen.height = var.grid.height*var.grid.blockwidth
		if (var.screen.full):
			var.py.screen = pygame.display.set_mode((var.screen.width,var.screen.height),pygame.FULLSCREEN)
		else:
			var.py.screen = pygame.display.set_mode((var.screen.width,var.screen.height),pygame.RESIZABLE)
		var.snake.x = random.randint(1,var.grid.width-2)
		var.snake.y = random.randint(1,var.grid.height-2)
		var.snake.length = 4
		var.snake.direction = 5
		var.snake.tail.x = []
		var.snake.tail.y = []
		var.apple.place()
		var.bomb.place()
		var.current.points = 0
		var.snake.speed = float(5)
class game:
	def start():
		var.setup()
		var.getvar(var.current.mode)
		game.draw.screen()
	def death():
		var.snake.deaths+=1
		if (var.current.highscore > var.current.points):
			game.draw.string(var.py.screen,var.grid.blockwidth,var.grid.blockwidth,50,"Game over!\nScore: "+str(var.current.points)+"\nHighScore: "+str(var.current.highscore),(255,0,0))
		elif (var.current.highscore <= var.current.points):
			game.draw.string(var.py.screen,var.grid.blockwidth,var.grid.blockwidth,50,"Game over!\nNew HighScore!\nHighScore: "+str(var.current.points),(255,0,0))
			var.current.highscore = var.current.points
			if(os.path.isfile("hs.data")):
				file = open("hs.data",'w')
				file.write(str(var.current.highscore))
				file.close()
			else:
				file = open("hs.data",'a')
				file.write(str(var.current.highscore))
				file.close()
		pygame.display.flip()
		time.sleep(1.5)
		var.setup()
		var.getvar(var.current.mode)
		game.draw.screen()
	class draw:
		def rec(s,x,y,w,h,c):
			pygame.draw.rect(s,c,pygame.Rect(x,y,w,h))
		def string(s,x,y,height,string,c):
			font = var.misc.font
			if(height != None):
				font = pygame.font.SysFont('Consolas', height)
			else:
				height = 15
			if (len(string.split("\n"))>0):
				for i in range(len(string.split("\n"))):
					text = font.render(string.split("\n")[i], False, c)
					s.blit(text,(x,y+(height*i)))
			else:
				text = font.render(string, False, c)
				s.blit(text,(x,y))
		def screen():
			screen = var.py.screen
			block_width = var.grid.blockwidth
			screen_width = var.screen.width
			screen_height = var.screen.height
			rec = game.draw.rec
			c1 = var.grid.color1
			c2 = var.grid.color2
			for x in range(int(var.grid.width)):
				for y in range(int(var.grid.width)):
					of = 0
					if (y%2)==0:
						of = 1
					if (((x+of)%2)==0):
						rec(screen,x*block_width,y*block_width,block_width,block_width,c1)

					else:
						rec(screen,x*block_width,y*block_width,block_width,block_width,c2)

			rec(screen,0,0,block_width,screen_height,(8,8,8))
			rec(screen,screen_width-block_width,0,block_width,screen_height,(8,8,8))
			rec(screen,0,0,screen_width,block_width,(8,8,8))
			rec(screen,0,screen_height-block_width,screen_height,block_width,(8,8,8))
			color=(246,0,0)
			if (var.bomb.enabled):
				rec(screen, block_width*var.bomb.x+2,block_width*var.bomb.y+2, block_width-4, block_width-4,color)
			color=var.apple.color
			rec(screen, block_width*var.apple.x+2,block_width*var.apple.y+2, block_width-4, block_width-4,color)
			color_offset = var.misc.coloroffset
			col = len(var.snake.tail.x)*color_offset
			for i in range(len(var.snake.tail.x)):
				if((col-color_offset) <= 0):
					color_offset=255
				else:
					col-=color_offset
				color = (col,col,192)
				rec(screen,block_width*var.snake.tail.x[i],block_width*var.snake.tail.y[i],block_width,block_width,color)
			color=var.snake.color
			rec(screen,block_width*var.snake.x,block_width*var.snake.y,block_width,block_width,color)
			game.draw.string(screen,0,0,25,"P: "+str(var.current.points)+"|HS: "+str(var.current.highscore)+"|V: "+str(var.snake.speed)+"|L: "+str(var.snake.length)+"|B/S",(255,255,255))
			pygame.display.flip()
	def ref():
		game.tails()
		dire = var.snake.direction
		var.snake.lastdir = var.snake.direction
		move = game.move
		if (dire== 0):
			move(0,-1)
			#snake.y -=1
		elif (dire == 1):
			move(1,0)
			#snake.x+=1
		elif (dire == 2):
			#snake.y+=1
			move(0,1)
		elif (dire == 3):
			move(-1,0)
			#snake.x-=1
	def move(x,y):
		death = game.death
		#x check
		if (var.snake.x+x)>= var.grid.width-1:
			if(var.rules.wallloop):
				var.snake.x = 1;
			else:
				death()
			#print ("out of bounds")

		elif(var.snake.x+x)<= 0:
			#print ("out of bounds")
			if(var.rules.wallloop):
				var.snake.x = var.grid.width-2;
			else:
				death()
		else:
			var.snake.x+=x
		#y check
		if (var.snake.y+y)>= var.grid.height-1:
			#print ("out of bounds")
			if(var.rules.wallloop):
				var.snake.y = 1;
			else:
				death()
		elif(var.snake.y+y)<= 0:
			#print ("out of bounds")
			if(var.rules.wallloop):
				var.snake.y = var.grid.height-2;
			else:
				death()
		else:
			var.snake.y+=y
		#  apple
		if (var.snake.x == var.apple.x) and (var.snake.y == var.apple.y):
			var.snake.length+=1
			var.current.points+=1
			var.apple.lvl+=1
			var.snake.speed += var.snake.accel
			print(var.snake.speed)
			var.apple.place()
			var.bomb.place()
		elif (var.snake.x == var.bomb.x) and (var.snake.y == var.bomb.y) and (var.bomb.enabled):
			
			death()
			var.bomb.place()
			
			print(var.bomb.enabled)
			#print("Apple pos:\nX - "+str(apple.x)+"\nY - "+str(apple.y))
		cdeaths = var.snake.deaths;
		for i in range(len(var.snake.tail.x)):
			if(var.snake.deaths == cdeaths):
				if (var.snake.x == var.snake.tail.x[i]):
					 if (var.snake.y == var.snake.tail.y[i]):
						 #print("game over")
						 death();
	def tails():
		var.snake.tail.x.append(var.snake.x)
		var.snake.tail.y.append(var.snake.y)
		if (len(var.snake.tail.x) > var.snake.length):
			var.snake.tail.x.pop(0)
			var.snake.tail.y.pop(0)
	def keyd():#direction checker and picker, needs work
		pressed = pygame.key.get_pressed()
		dire = var.snake.lastdir
		ndire = var.snake.direction
		if pressed[pygame.K_UP]:
			if(dire != 2):
				ndire=0
		if pressed[pygame.K_RIGHT]:
			if(dire != 3):
				ndire=1
		if pressed[pygame.K_DOWN]:
			if(dire != 0):
				ndire=2
		if pressed[pygame.K_LEFT]:
			if(dire != 1):
				ndire=3
		var.snake.direction = ndire
		if pressed[pygame.K_z]:
			var.screen.full = not var.screen.full
			var.setup()
class menu:
	def gsetup():
		var.screen.width= 120
	def setup():
		var.screen.width = 300
		var.screen.height = 80
		var.modes()
		menu.menu2 = var.misc.modes
		print(var.misc.modes)
	menu1 = ["Play","Quit"]
	menu2 = ["Easy","Medium","Hard"]
	menu = 1
	button = 0
	class draw:
		def rec(s,x,y,w,h,c):
			pygame.draw.rect(s,c,pygame.Rect(x,y,w,h))
		def string(s,x,y,height,string,c):
			font = var.misc.font
			if(height != None):
				font = pygame.font.SysFont('Consolas', height)
			else:
				height = 15
			if (len(string.split("\n"))>0):
				for i in range(len(string.split("\n"))):
					text = font.render(string.split("\n")[i], False, c)
					s.blit(text,(x,y+(height*i)))
			else:
				text = font.render(string, False, c)
				s.blit(text,(x,y))
		def btn(s,x,y,w,h,c1,c2,st):
			menu.draw.rec(s,x,y,w,h,c1)
			menu.draw.string(s,x,y,h,st,c2)
		def draw():
			s = var.py.screen
			lmenu = []
			if menu.menu == 1:
				lmenu = menu.menu1
			elif menu.menu == 2:
				lmenu = menu.menu2

			for i in range(len(lmenu)):
				if i == menu.button:
					menu.draw.btn(s,0,20*i,200,20,(80,90,100),(230,240,250),lmenu[i])
				else:
					menu.draw.btn(s,0,20*i,200,20,(20,30,40),(200,210,220),lmenu[i])
	def keyd():
		if (pygame.key.get_pressed()[pygame.K_RIGHT]) or (pygame.key.get_pressed()[pygame.K_RETURN]):
			if (menu.menu == 1):
				if (menu.button == 0):
					menu.menu = 2
					menu.button = 0
				else:
					quit();
			else:

				game.start()
				var.current.mode = menu.button
				var.getvar(menu.button)
				var.misc.scene+=1

		elif(pygame.key.get_pressed()[pygame.K_DOWN]):
			if menu.menu == 1:
				if(menu.button+1 <= len(menu.menu1)-1):
					menu.button += 1
				else:
					menu.button = 0
				print(menu.button)
			elif menu.menu == 2:
				if(menu.button+1 <= len(menu.menu2)-1):
					menu.button += 1
				else:
					menu.button = 0
				print(menu.button)
		elif(pygame.key.get_pressed()[pygame.K_UP]):
			if(menu.button-1 >= 0):
				menu.button -= 1
			else:
				menu.button = 0
			print(menu.button)

			









def loop():
	c = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
				quit()

		# gamef.grid()
		if (var.misc.scene == 0):

			menu.draw.draw()
			pygame.display.flip()
			var.py.clock.tick(10)
			menu.keyd()
			
		elif (var.misc.scene == 1):
			game.keyd()
			c+=1
			game.draw.screen()
			if (c >= (var.py.tick/var.snake.speed)):
				game.ref()
				c=0
				#snake.speed+=1
			if not(var.snake.direction  == 5):
				pygame.display.set_caption("Snake!!!|Score: "+str(var.current.points))
			pygame.display.flip()
			var.py.clock.tick(var.py.tick)
try:
	menu.setup()
	loop()
except  Exception as e:
	print(e)
	log = open("snakegame-error.log",'a')
	log.write("Error"+str(e)+"\n")
	log.close()
loop()

