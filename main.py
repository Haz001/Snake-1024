import pygame
import time
from dataclasses import dataclass

class Point:
    """
    A 2 Dimensional Coordinate Type

    :attr:
        x - X Coordinate
        y - Y Coordinate
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{(self.x, self.y,)}'

    def __repr__(self):
        class_name = self.__class__.__name__
        # formatted string, !r - shorthand for repr
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    def __iter__(self):
        """
        :return: tuple of x, y
        """
        return iter((
            self.x,
            self.y,
        ))
    @property 
    def as_tuple(self):
        return (self.x, self.y)
    @property 
    def as_list(self):
        return [self.x, self.y]

    def __eq__(self, other):
        tother: str = type(other).__name__
        result: bool
        match tother:
            case str(self.__class__.__name__):
                result = (self.x == other.x) and (self.y == other.y)
            case "tuple":
                result = self.as_tuple == other
            case "list":
                result = self.as_list == other
            case _:
                print(f"Can't compare {tother} to {self.__class__}")
                result = False
        return result

    def __getitem__(self, key):
        if isinstance(key, int):
            try:
                self.as_tuple[key]
            except IndexError as e:
                print(e)
                raise IndexError(f"{self.__class__.__name__} index out of range")

    def __round__(self, n):
        x = self.x.__round__(n)
        y = self.y.__round__(n)
        return self.__init__(x, y)

    def __floor__(self):
        x = self.x.__floor__()
        y = self.y.__floor__()
        return self.__init__(x, y)

    def __ceil__(self):
        x = self.x.__ceil__()
        y = self.y.__ceil__()
        return self.__init__(x, y)


@dataclass
class controller:
    up = pygame.K_UP
    left = pygame.K_LEFT
    right = pygame.K_RIGHT
    down = pygame.K_DOWN


@dataclass
class Snake:
    loc = Point(0, 0)
    speed = Point(1, 1)
    size = Point(60,60)

    last_tick = time.time()

    def draw(self, scr: pygame.Surface):
        pygame.draw.rect(scr, pygame.Color(56,32,216), pygame.Rect(self.loc.x,self.loc.y,self.size.x,self.size.y))

    def tick(self):
        current_time = time.time()
        last_tick = self.last_tick
        delta_time = current_time-last_tick

        # ToDo: set last tick to new tick
        # its funny without it, speed increases
        # with time, but it should be done at.
        
        self.loc.x += self.speed.x*delta_time
        self.loc.y += self.speed.y*delta_time
        if (self.size.x+self.loc.x >= 1280) or self.loc.x <= 0:
            self.speed.x = -self.speed.x
        if (self.size.y+self.loc.y >= 720) or self.loc.y <= 0:
            self.speed.y = -self.speed.y





snake = Snake()
if __name__ == "__main__":
    running = True
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()



    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                pass


        screen.fill("grey")
        
        snake.draw(screen)
        snake.tick()

        pygame.display.flip()
        
        clock.tick(600)
    pygame.quit()
