import pygame as py
import random as rn
py.init()
class gm:
    clk=py.time.Clock()
    scr=py.display.set_mode((512,512))
    run=True
    class sn:
        x = rn.randint(0,32)
        y = rn.randint(0,32)
    def rec(s,x,y,w,h,c):
        py.draw.rect(s,c,py.Rect(x,y,w,h))
    def draw():
        gm.rec(gm.scr,gm.sn.x*16,gm.sn.y*16,32,32,(255,0,0))
while gm.run:
    gm.draw()
    py.display.flip()
