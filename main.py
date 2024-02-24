import pygame
import time
from dataclasses import dataclass
from Point import *
import itertools
from enum import Enum
import math

pixel_size = Point(20,20)
screen_size = Point(80*pixel_size.x,45*pixel_size.y)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    DOWN = 3
    UP = 4

@dataclass
class controller:
    right = [pygame.K_RIGHT, pygame.K_d]
    left = [pygame.K_LEFT, pygame.K_a]
    down = [pygame.K_DOWN, pygame.K_s]
    up = [pygame.K_UP, pygame.K_w]
    pause = [pygame.K_ESCAPE]



class Snake:
    loc: Point
    speed: Point
    size: int
    last_tick: float
    tail_size: int
    tail: list[Point]
    def __init__(self):
        self.loc = Point(0, 0)
        self.speed = Point(600, 600)
        self.size = pixel_size 
        self.last_tick = time.time()
        self.tail_size = 1
        self.tail = list()


    def draw(self, scr: pygame.Surface):
        x = round((self.loc.x/self.size.x)-0.5)*self.size.x
        y = round((self.loc.y/self.size.y)-0.5)*self.size.y
        pygame.draw.rect(
            scr,
            pygame.Color(56, 32, 216),
            pygame.Rect(x, y, self.size.x, self.size.y),
        )
        #pygame.draw.circle(
        #    scr,
        #    pygame.Color(216, 32,56 ),
        #    self.loc.as_tuple,
        #    4
        #)

    def tick(self):
        current_tick = time.time()   # Current time
        last_tick = self.last_tick   # Previous tick time
        self.last_tick = current_tick   # Set new last current tick
        delta_tick = current_tick - last_tick   # delta time

        # Calculate new location with speed
        self.loc.x += self.speed.x * delta_tick
        self.loc.y += self.speed.y * delta_tick
        if self.size.x + self.loc.x >= screen.get_size()[0]:
            self.speed.x = -abs(self.speed.x)
        elif self.loc.x <= 0:
            self.speed.x = abs(self.speed.x)
        if self.size.y + self.loc.y >= screen.get_size()[1]:
            self.speed.y = -abs(self.speed.y)
        elif self.loc.y <= 0:
            self.speed.y = abs(self.speed.y)

    def change_direction(self, direction: Direction):
        centre = lambda uncentred, box_delta: (round(uncentred/box_delta)+0.5)*box_delta
            
        if direction == Direction.RIGHT:
            self.loc.y = centre(self.loc.y, pixel_size.y)
            self.speed = Point(speed, 0)
        elif direction == Direction.LEFT:
            self.loc.y = centre(self.loc.y, pixel_size.y)
            self.speed = Point(-speed, 0)
        elif direction == Direction.DOWN:
            self.loc.x = centre(self.loc.x, pixel_size.x)
            self.speed = Point(0, speed)
        elif direction == Direction.UP:
            self.loc.x = centre(self.loc.x, pixel_size.x)
            self.speed = Point(0, -speed)




snake: Snake
if __name__ == '__main__':
    running = True
    pygame.init()
    screen = pygame.display.set_mode(screen_size.as_tuple)
    clock = pygame.time.Clock()
    speed = pixel_size.x*10
    snake = Snake()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in controller.right:
                    snake.change_direction(Direction.RIGHT)
                elif event.key in controller.left:
                    snake.change_direction(Direction.LEFT)
                elif event.key in controller.down:
                    snake.change_direction(Direction.DOWN)
                elif event.key in controller.up:
                    snake.change_direction(Direction.UP)
        screen.fill('grey')
        snake.tick()

        snake.draw(screen)

        pygame.display.flip()

        clock.tick(60)
    pygame.quit()
