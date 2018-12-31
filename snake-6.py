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
except:
    print("----<error>-----\nProblem with imported modules\nModules|Imported\nrandom |"+str(a)+"\ntime   |"+str(b)+"\threading   |"+str(c)+"\nPlease fix")


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
        class rules:
            wallloop = False
        class misc:
            coloroffset = 4
        class current:
            points = 0
            deaths = 0
            state = 0
        class py:
            clock = pygame.time.Clock()
            screen = pygame.display.set_mode((100, 100))
        def getvar():
            file = open("var.data",'r')
            print(file.read())
            file.close()
        class apple:
            color = (0,255,0)
            x = 0
            y = 0
            lvl = 0
            # def place():
            #     apple.x = random.randint(1,vr.gw-2)
            #     apple.y = random.randint(1,vr.gh-2)
            #     while not(check(apple.x, apple.y)):
            #         apple.x = random.randint(1,vr.gw-2)
            #         apple.y = random.randint(1,vr.gh-2)
        class snake:
            color = (0,0,192)
            length = 4
            x = 0
            y = 0
            direction = 5
            speed = 10
            class tail:
                x = []
                y = []


        def setup():
            game.var.screen.width = game.var.grid.width*game.var.grid.blockwidth
            game.var.screen.height = game.var.grid.height*game.var.grid.blockwidth
            game.var.py.screen = pygame.display.set_mode((game.var.screen.width,game.var.screen.height))
            game.var.snake.x = random.randint(1,game.var.grid.width-2)
            game.var.snake.y = random.randint(1,game.var.grid.height-2)
            game.var.apple.x = random.randint(1,game.var.grid.width-2)
            game.var.apple.y = random.randint(1,game.var.grid.height-2)
            print("Screen: Setup")
            print("done")
    class fun:
        def start():
            game.var.setup()
            game.fun.draw.screen()
        class draw:
            def rec(s,x,y,w,h,c):
                pygame.draw.rect(s,c,pygame.Rect(x,y,w,h))
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
                pygame.display.flip()
        #====< Not done >=====#
        def ref():
            game.fun.tails()
            dir = game.var.snake.direction
            move = game.fun.move
            if (dir== 0):
                move(0,-1)
                #snake.y -=1
            elif (dir == 1):
                move(1,0)
                #snake.x+=1
            elif (dir == 2):
                #snake.y+=1
                move(0,1)
            elif (dir == 3):
                move(-1,0)
                #snake.x-=1
        def move(x,y):
            death = game.fun.start
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
            #
            # #apple
            # if (snake.x == apple.x) and (snake.y == apple.y):
            #     snake.leng+=1
            #     apple.lvl+=1
            #
            #     apple.place()
            #     bomb.place()
            # elif (snake.x == bomb.x) and (snake.y == bomb.y):
            #     death()
            #     bomb.x = random.randint(1,vr.gw-2)
            #     bomb.y = random.randint(1,vr.gh-2)
            #     #print("Apple pos:\nX - "+str(apple.x)+"\nY - "+str(apple.y))
            # cdeaths = snake.deaths;
            # for i in range(len(snake.tailx)):
            #     if(snake.deaths == cdeaths):
            #         if (snake.x == snake.tailx[i]):
            #              if (snake.y == snake.taily[i]):
            #                  #print("game over")
            #                  death();
        def tails():
            game.var.snake.tail.x.append(game.var.snake.x)
            game.var.snake.tail.y.append(game.var.snake.y)
            if (len(game.var.snake.tail.x) > game.var.snake.length):
                game.var.snake.tail.x.pop(0)
                game.var.snake.tail.y.pop(0)
        def keyd():
            pressed = pygame.key.get_pressed()
            dir = game.var.snake.direction
            ndir = dir
            if pressed[pygame.K_UP]:
                if(dir != 2):
                    ndir=0
            if pressed[pygame.K_RIGHT]:
                if(dir != 3):
                    ndir=1
            if pressed[pygame.K_DOWN]:
                if(dir != 0):
                    ndir=2
            if pressed[pygame.K_LEFT]:
                if(dir != 1):
                    ndir=3
            game.var.snake.direction = ndir

print("starting")
game.fun.start()
c = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            quit()

    # gamef.grid()
    game.fun.keyd()
    c+=1
    game.fun.draw.screen()
    if (c >= (100/10)):
        game.fun.ref()
        c=0
        #snake.speed+=1
    if not(game.var.snake.direction  == 5):
        pygame.display.set_caption("Snake!!!|Score: "+str(game.var.snake.length-4))
    pygame.display.flip()
    game.var.py.clock.tick(100)
