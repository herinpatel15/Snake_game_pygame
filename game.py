import pygame as pg
import time 

from snake import Snake 
from food import Food

class Game:
    def __init__(self):
        pg.init()
        self.win = pg.display.set_mode((1000, 800))
        self.win.fill((0, 0, 0))
        pg.display.set_caption("hello Snake 🐍")
        self.snake = Snake(x=30, y=30, snakeSize=20, win=self.win, length=6)
        self.speed = 0.1
        self.food = Food(win=self.win, foodSize=10)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2 + 10:
            if y1 >= y2 and y1 <= y2 + 10:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.food.draw()
        self.score()
        pg.display.flip()

        # * food collision
        if self.is_collision(self.food.x, self.food.y, self.snake.x[0], self.snake.y[0]):
            self.food.place()
            self.snake.snake_size()

        # * head collision
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[i], self.snake.y[i], self.snake.x[0], self.snake.y[0]):
                raise "Game Over"

    def game_over(self):
        self.win.fill((0, 0, 0))
        font = pg.font.SysFont("arial", 30)
        score = font.render(
            f"Score: {self.snake.length - 6}", True, (255, 255, 255))
        self.win.blit(score, (200, 300))
        line = font.render(
            "To play again press ENTER, To exite press ESCAPE", True, (255, 255, 255))
        self.win.blit(line, (200, 350))
        pg.display.flip()

    def reset(self):
        self.snake = Snake(x=30, y=30, snakeSize=20, win=self.win, length=6)
        self.food = Food(win=self.win, foodSize=10)

    def score(self):
        font = pg.font.SysFont("arial", 30)
        score = font.render(
            f"Score: {self.snake.length - 6}", True, (255, 255, 255))
        self.win.blit(score, (800, 10))

    def run(self):
        self.run = True
        self.pause = False
        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False

                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.run = False

                    elif event.key == pg.K_RETURN:
                        self.pause = False
                        self.reset()

                    elif event.key == pg.K_w or event.key == pg.K_UP:
                        if self.snake.direction != "down":
                            self.snake.direction = "up"

                    elif event.key == pg.K_d or event.key == pg.K_RIGHT:
                        if self.snake.direction != "left":
                            self.snake.direction = "right"

                    elif event.key == pg.K_s or event.key == pg.K_DOWN:
                        if self.snake.direction != "up":
                            self.snake.direction = "down"

                    elif event.key == pg.K_a or event.key == pg.K_LEFT:
                        if self.snake.direction != "right":
                            self.snake.direction = "left"

            try:
                if not self.pause:
                    self.play()
            except Exception as e:
                self.game_over()
                self.pause = True

            time.sleep(self.speed)
