import random
import pygame as pg 

class Food:
    def __init__(self, win, foodSize):
        self.win = win
        self.x = 20 * 3
        self.y = 20 * 3
        self.foodSize = foodSize

    def draw(self):
        pg.draw.circle(self.win, (255, 255, 255), (self.x, self.y), 10)
        pg.display.flip()

    def place(self):
        self.x = random.randint(1, 24) * 40
        self.y = random.randint(1, 19) * 40
