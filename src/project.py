import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Ball:
    def __init__(self, x, y, dx, dy, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off the top and bottom walls
        if self.y - self.radius < 0 or self.y + self.radius > SCREEN_HEIGHT:
            self.dy *= -1


def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()