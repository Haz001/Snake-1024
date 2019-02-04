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
class game:
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
			font = pygame.font.SysFont('Consolas', 15)
			coloroffset = 4
			scene = 0
		class current:
			highscore = 0
			points = 0
			deaths = 0
			state = 0
		class py:
			tick = 100
			clock = pygame.time.Clock()
			screen = pygame.display.set_mode((100, 100))
		def getvar():

##			file = open("var.data",'r')
##			print(file.read())
##			file.close()
			print("To be added")
		class apple:
			color = (0,255,0)
			x = 0
			y = 0
			lvl = 0
			def place():
				game.var.apple.x = random.randint(1,game.var.grid.width-2)
				game.var.apple.y = random.randint(1,game.var.grid.height-2)
				# while not(check(game.var.apple.x, game.var.apple.y)):
				#	 game.var.apple.x = random.randint(1,game.var.grid.width-2)
				#	 game.var.apple.y = random.randint(1,game.var.grid.height-2)
		class bomb:
			color = (0,255,0)
			x = 0
			y = 0
			lvl = 0
			def place():
				game.var.bomb.x = random.randint(1,game.var.grid.width-2)
				game.var.bomb.y = random.randint(1,game.var.grid.height-2)
				while (4>((game.var.bomb.x-game.var.apple.x)**2+(game.var.bomb.y-game.var.apple.y)**2)**0.5):
					 game.var.bomb.x = random.randint(1,game.var.grid.width-2)
					 game.var.bomb.y = random.randint(1,game.var.grid.height-2)
		class snake:
			color = (0,0,192)
			length = 4
			x = 0
			y = 0
			direction = 5
			speed = float(5)
			deaths = 0
			class tail:
				x = []
				y = []


		def setup():
			if(os.path.isfile("hs.data")):
				try:
					file = open("hs.data",'r')
					game.var.current.highscore = int(file.read())
					file.close()
				except:
					game.var.current.highscore = 0
			else:
				game.var.current.highscore = 0
			game.var.screen.width = game.var.grid.width*game.var.grid.blockwidth
			game.var.screen.height = game.var.grid.height*game.var.grid.blockwidth
			if (game.var.screen.full):
				game.var.py.screen = pygame.display.set_mode((game.var.screen.width,game.var.screen.height),pygame.FULLSCREEN)
			else:
				game.var.py.screen = pygame.display.set_mode((game.var.screen.width,game.var.screen.height),pygame.RESIZABLE)
			game.var.snake.x = random.randint(1,game.var.grid.width-2)
			game.var.snake.y = random.randint(1,game.var.grid.height-2)
			game.var.snake.length = 4
			game.var.snake.direction = 5
			game.var.snake.tail.x = []
			game.var.snake.tail.y = []
			game.var.apple.place()
			game.var.bomb.place()
			game.var.current.points = 0
			game.var.snake.speed = 5
	class fun:
		def start():
			game.var.setup()
			game.fun.draw.screen()
		def death():
			game.var.snake.deaths+=1
			if (game.var.current.highscore > game.var.current.points):
				game.fun.draw.string(game.var.py.screen,game.var.grid.blockwidth,game.var.grid.blockwidth,50,"Game over!\nScore: "+str(game.var.current.points)+"\nHighScore: "+str(game.var.current.highscore),(255,0,0))
			elif (game.var.current.highscore <= game.var.current.points):
				game.fun.draw.string(game.var.py.screen,game.var.grid.blockwidth,game.var.grid.blockwidth,50,"Game over!\nNew HighScore!\nHighScore: "+str(game.var.current.points),(255,0,0))
				game.var.current.highscore = game.var.current.points
				if(os.path.isfile("hs.data")):
					file = open("hs.data",'w')
					file.write(str(game.var.current.highscore))
					file.close()
				else:
					file = open("hs.data",'a')
					file.write(str(game.var.current.highscore))
					file.close()
			pygame.display.flip()
			time.sleep(1.5)
			game.var.setup()
			game.fun.draw.screen()
		class draw:
			def rec(s,x,y,w,h,c):
				pygame.draw.rect(s,c,pygame.Rect(x,y,w,h))
			def string(s,x,y,height,string,c):
				font = game.var.misc.font
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
				screen = game.var.py.screen
				block_width = game.var.grid.blockwidth
				screen_width = game.var.screen.width
				screen_height = game.var.screen.height
				rec = game.fun.draw.rec
				c1 = game.var.grid.color1
				c2 = game.var.grid.color2
				for x in range(int(game.var.grid.width)):
					for y in range(int(game.var.grid.width)):
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
				color=(255,0,0)
				rec(screen, block_width*game.var.bomb.x+2,block_width*game.var.bomb.y+2, block_width-4, block_width-4,color)
				color=game.var.apple.color
				rec(screen, block_width*game.var.apple.x+2,block_width*game.var.apple.y+2, block_width-4, block_width-4,color)
				color_offset = game.var.misc.coloroffset
				col = len(game.var.snake.tail.x)*color_offset
				for i in range(len(game.var.snake.tail.x)):
					if((col-color_offset) <= 0):
						color_offset=255
					else:
						col-=color_offset
					color = (col,col,192)
					rec(screen,block_width*game.var.snake.tail.x[i],block_width*game.var.snake.tail.y[i],block_width,block_width,color)
				color=game.var.snake.color
				rec(screen,block_width*game.var.snake.x,block_width*game.var.snake.y,block_width,block_width,color)
				game.fun.draw.string(screen,0,0,25,"P: "+str(game.var.current.points)+"|HS: "+str(game.var.current.highscore)+"|V: "+str(game.var.snake.speed)+"B/S",(255,255,255))
				pygame.display.flip()
		def ref():
			game.fun.tails()
			dire = game.var.snake.direction
			move = game.fun.move
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
			death = game.fun.death
			#x check
			if (game.var.snake.x+x)>= game.var.grid.width-1:
				if(game.var.rules.wallloop):
					game.var.snake.x = 1;
				else:
					death()
				#print ("out of bounds")

			elif(game.var.snake.x+x)<= 0:
				#print ("out of bounds")
				if(game.var.rules.wallloop):
					snake.x = vr.gw-2;
				else:
					death()
			else:
				game.var.snake.x+=x
			#y check
			if (game.var.snake.y+y)>= game.var.grid.height-1:
				#print ("out of bounds")
				if(game.var.rules.wallloop):
					snake.y = 1;
				else:
					death()
			elif(game.var.snake.y+y)<= 0:
				#print ("out of bounds")
				if(game.var.rules.wallloop):
					game.var.snake.y = vr.game.var.grid.height-2;
				else:
					death()
			else:
				game.var.snake.y+=y
			#  apple
			if (game.var.snake.x == game.var.apple.x) and (game.var.snake.y == game.var.apple.y):
				game.var.snake.length+=1
				game.var.current.points+=1
				game.var.apple.lvl+=1
				game.var.snake.speed += 0.5
				print(game.var.snake.speed)
				game.var.apple.place()
				game.var.bomb.place()
			elif (game.var.snake.x == game.var.bomb.x) and (game.var.snake.y == game.var.bomb.y):
				death()
				game.var.bomb.place()
				#print("Apple pos:\nX - "+str(apple.x)+"\nY - "+str(apple.y))
			cdeaths = game.var.snake.deaths;
			for i in range(len(game.var.snake.tail.x)):
				if(game.var.snake.deaths == cdeaths):
					if (game.var.snake.x == game.var.snake.tail.x[i]):
						 if (game.var.snake.y == game.var.snake.tail.y[i]):
							 #print("game over")
							 death();
		def tails():
			game.var.snake.tail.x.append(game.var.snake.x)
			game.var.snake.tail.y.append(game.var.snake.y)
			if (len(game.var.snake.tail.x) > game.var.snake.length):
				game.var.snake.tail.x.pop(0)
				game.var.snake.tail.y.pop(0)
		def keyd():#direction checker and picker, needs work
			pressed = pygame.key.get_pressed()
			dire = game.var.snake.direction
			ndire = dire
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
			game.var.snake.direction = ndire
			if pressed[pygame.K_z]:
				game.var.screen.full = not game.var.screen.full
				game.var.setup()
class menu:
	def gsetup():
		game.var.screen.width= 120
	def setup():
		game.var.screen.width = 300
		game.var.screen.height = 80
	menu1 = ["Play","Quit"]
	menu2 = ["Easy","Medium","Hard"]
	menu = 1
	button = 0
	class draw:
		def rec(s,x,y,w,h,c):
			pygame.draw.rect(s,c,pygame.Rect(x,y,w,h))
		def string(s,x,y,height,string,c):
			font = game.var.misc.font
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
			s = game.var.py.screen
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

			


print("starting")
menu.setup()






def loop():
	c = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
				quit()

		# gamef.grid()
		if (game.var.misc.scene == 0):

			menu.draw.draw()
			pygame.display.flip()
			game.var.py.clock.tick(10)

			if (pygame.key.get_pressed()[pygame.K_RIGHT]) or (pygame.key.get_pressed()[pygame.K_RETURN]):
				if (menu.menu == 1):
					if (menu.button == 0):
						menu.menu = 2
						menu.button = 0
					else:
						quit();
				else:
					game.fun.start()
					game.var.misc.scene+=1
			elif(pygame.key.get_pressed()[pygame.K_DOWN]):
				if(menu.button+1 <= len(menu.menu1)-1):
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
		elif (game.var.misc.scene == 1):
			game.fun.keyd()
			c+=1
			game.fun.draw.screen()
			if (c >= (game.var.py.tick/game.var.snake.speed)):
				game.fun.ref()
				c=0
				#snake.speed+=1
			if not(game.var.snake.direction  == 5):
				pygame.display.set_caption("Snake!!!|Score: "+str(game.var.current.points))
			pygame.display.flip()
			game.var.py.clock.tick(game.var.py.tick)
try:
	loop()
except  Exception as e:
	print(e)
	log = open("snakegame-error.log",'a')
	log.write("Error"+str(e)+"\n")
	log.close()
loop()

