import pygame as pg

class Snake:
    def __init__(self, x, y, snakeSize, win, length):
        self.length = length
        self.x = [x] * length
        self.y = [y] * length
        self.snakeSize = snakeSize
        self.win = win
        self.direction = "right"

    def draw(self):
        self.win.fill((0, 0, 0))
        for i in range(self.length):
            pg.draw.rect(self.win, (255, 0, 0), pg.Rect(
                self.x[i], self.y[i], self.snakeSize, self.snakeSize))
        pg.display.flip()

    def snake_size(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_up(self):
        self.y[0] -= self.snakeSize
        self.draw()

    def move_right(self):
        self.x[0] += self.snakeSize
        self.draw()

    def move_down(self):
        self.y[0] += self.snakeSize
        self.draw()

    def move_left(self):
        self.x[0] -= self.snakeSize
        self.draw()

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == "right":
            self.move_right()

        elif self.direction == "left":
            self.move_left()

        elif self.direction == "up":
            self.move_up()

        elif self.direction == "down":
            self.move_down()
