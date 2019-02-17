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
class vr:
    #grid width
    gw = 16
    #grid height
    gh = 16
    #square size
    pxl = 32
    #screen width
    sw = 0
    #screen height
    sh = 0
    #wall loop
    wl = False
    #points
    points = 0
    #color offset
    coloroffset = 8
    #is the game over
    done = False

vr.sw = vr.gw*vr.pxl
vr.sh = vr.gh*vr.pxl
#setup
clock = pygame.time.Clock()
screen = pygame.display.set_mode((vr.sw, vr.sh))
#pressed = pygame.key.get_pressed()
c = 0;

class apple:
    x = random.randint(1,vr.gw-2)
    y = random.randint(1,vr.gh-2)
    lvl = 0
    def place():
        apple.x = random.randint(1,vr.gw-2)
        apple.y = random.randint(1,vr.gh-2)
        while not(gamef.check(apple.x, apple.y)):
            apple.x = random.randint(1,vr.gw-2)
            apple.y = random.randint(1,vr.gh-2)


class bomb:
    x = random.randint(1,vr.gw-2)
    y = random.randint(1,vr.gh-2)
    def place():
        bomb.x = random.randint(1,vr.gw-2)
        bomb.y = random.randint(1,vr.gh-2)
        while not(gamef.check(apple.x, apple.y)):
            bomb.x = random.randint(1,vr.gw-2)
            bomb.y = random.randint(1,vr.gh-2)
class snake:
    ##x first then y
    leng = 4
    x = random.randint(1,vr.gw-2)
    y = random.randint(1,vr.gh-2)
    dire = 5
    speed = 10
    tailx = []
    taily = []
    deaths = 0

class gamef:
    def check(x,y):
        for i in range(len(snake.tailx)):
            if(x == snake.tailx[i]):
                if(y == snake.taily[i]):
                    return False
        return True

    def death():
        snake.leng = 4
        snake.x = random.randint(1,vr.gw-2)
        snake.y = random.randint(1,vr.gh-2)
        snake.dire = 5
        snake.speed = 10
        snake.tailx = []
        snake.taily = []
        snake.deaths +=1;
        time.sleep(0.5)
        snake.dire = 5

    def grid():
        ty = False
        for x in range(int(vr.sw/vr.pxl)):
            for y in range(int(vr.sh/vr.pxl)):
                of = 0
                if (y%2)==0:
                    of = 1
                if (((x+of)%2)==0):
                    pygame.draw.rect(screen, (32,32,32),pygame.Rect(x*vr.pxl,y*vr.pxl,vr.pxl,vr.pxl))

                else:
                    pygame.draw.rect(screen, (64,64,64),pygame.Rect(x*vr.pxl,y*vr.pxl,vr.pxl,vr.pxl))
                ty = not ty
    def draw():
        #Framerate of 10
        pygame.draw.rect(screen, (8,8,8),pygame.Rect(0,0,vr.pxl,vr.sh))
        pygame.draw.rect(screen, (8,8,8),pygame.Rect(vr.sw-vr.pxl,0,vr.pxl,vr.sh))
        pygame.draw.rect(screen, (8,8,8),pygame.Rect(0,0,vr.sw,vr.pxl))
        pygame.draw.rect(screen, (8,8,8),pygame.Rect(0,vr.sh-vr.pxl,vr.sw,vr.pxl))
        color=(255,0,0)
        pygame.draw.rect(screen, color, pygame.Rect(vr.pxl*bomb.x+2,vr.pxl*bomb.y+2, vr.pxl-4, vr.pxl-4))
        color=(0,255,0)
        pygame.draw.rect(screen, color, pygame.Rect(vr.pxl*apple.x+2,vr.pxl*apple.y+2, vr.pxl-4, vr.pxl-4))
        os = vr.coloroffset
        col = len(snake.tailx)*os
        print(col)
        for i in range(len(snake.tailx)):
            if((col-os) <= 0):
                os=255
            else:
                col-=os

            color = (col,col,192)

            pygame.draw.rect(screen, color, pygame.Rect(vr.pxl*snake.tailx[i],vr.pxl*snake.taily[i], vr.pxl, vr.pxl))
        color=(0,0,192)
        pygame.draw.rect(screen, color, pygame.Rect(vr.pxl*snake.x,vr.pxl*snake.y, vr.pxl, vr.pxl))
    def keyd():
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if(snake.dire != 2):
                snake.dire=0
        if pressed[pygame.K_RIGHT]:
            if(snake.dire != 3):
                snake.dire=1
        if pressed[pygame.K_DOWN]:
            if(snake.dire != 0):
                snake.dire=2
        if pressed[pygame.K_LEFT]:
            if(snake.dire != 1):
                snake.dire=3
    def ref():
        gamef.tails()
        if (snake.dire == 0):
            gamef.move(0,-1)
            #snake.y -=1
        elif (snake.dire == 1):
            gamef.move(1,0)
            #snake.x+=1
        elif (snake.dire == 2):
            #snake.y+=1
            gamef.move(0,1)
        elif (snake.dire == 3):
            gamef.move(-1,0)
            #snake.x-=1
    def move(x,y):
        #x check
        if (snake.x+x)>= vr.gw-1:
            if(vr.wl):
                snake.x = 1;
            else:
                gamef.death()
            #print ("out of bounds")

        elif(snake.x+x)<= 0:
            #print ("out of bounds")
            if(vr.wl):
                snake.x = vr.gw-2;
            else:
                gamef.death()
        else:
            snake.x+=x
        #y check
        if (snake.y+y)>= vr.gh-1:
            #print ("out of bounds")
            if(vr.wl):
                snake.y = 1;
            else:
                gamef.death()
        elif(snake.y+y)<= 0:
            #print ("out of bounds")
            if(vr.wl):
                snake.y = vr.gh-2;
            else:
                gamef.death()

        else:
            snake.y+=y
        #apple
        if (snake.x == apple.x) and (snake.y == apple.y):
            snake.leng+=1
            apple.lvl+=1

            apple.place()
            bomb.place()
        elif (snake.x == bomb.x) and (snake.y == bomb.y):
            gamef.death()
            bomb.x = random.randint(1,vr.gw-2)
            bomb.y = random.randint(1,vr.gh-2)
            #print("Apple pos:\nX - "+str(apple.x)+"\nY - "+str(apple.y))
        cdeaths = snake.deaths;
        for i in range(len(snake.tailx)):
            if(snake.deaths == cdeaths):
                if (snake.x == snake.tailx[i]):
                     if (snake.y == snake.taily[i]):
                         #print("game over")
                         gamef.death();
    def tails():
        snake.tailx.append(snake.x)
        snake.taily.append(snake.y)
        if (len(snake.tailx) > snake.leng):
            snake.tailx.pop(0)
            snake.taily.pop(0)


while not vr.done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            vr.done = True
            exit()
            quit()

    gamef.grid()
    gamef.keyd()
    c+=1
    gamef.draw()
    if (c >= (100/snake.speed)):
        gamef.ref()
        c=0
        #snake.speed+=1
    if not(snake.dire  == 5):
        pygame.display.set_caption("Snake!!!|Score: "+str(snake.leng-4))
    pygame.display.flip()
    clock.tick(100)
