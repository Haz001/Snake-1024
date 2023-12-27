import pygame
import time
from dataclasses import dataclass
from Point import *
import itertools

pixel_size = Point(20,20)
screen_size = Point(80*pixel_size.x,45*pixel_size.y)

@dataclass
class controller:
    up = [pygame.K_UP, pygame.K_w]
    left = [pygame.K_LEFT, pygame.K_a]
    right = [pygame.K_RIGHT, pygame.K_d]
    down = [pygame.K_DOWN, pygame.K_s]
    pause = [pygame.K_ESCAPE]

@dataclass
class Snake:
    loc = Point(0, 0)
    speed = Point(600, 600)
    size = pixel_size 
    
    last_tick = time.time()

    def draw(self, scr: pygame.Surface):
        x = round(self.loc.x/self.size.x)*self.size.x
        y = round(self.loc.y/self.size.y)*self.size.y
        pygame.draw.rect(
            scr,
            pygame.Color(56, 32, 216),
            pygame.Rect(x, y, self.size.x, self.size.y),
        )
        pygame.draw.circle(
            scr,
            pygame.Color(216, 32,56 ),
            self.loc.as_tuple,
            4
        )

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
                if event.key in controller.up:
                    snake.speed = Point(0, -speed)
                elif event.key in controller.left:
                    snake.speed = Point(-speed, 0)
                elif event.key in controller.right:
                    snake.speed = Point(speed, 0)
                elif event.key in controller.down:
                    snake.speed = Point(0, speed)
        screen.fill('grey')
        snake.tick()

        snake.draw(screen)

        pygame.display.flip()

        clock.tick(60)
    pygame.quit()
