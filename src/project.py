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
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 5
    
    def move(self, direction):
        if direction == "up" and self.y > 0:
            self.y -= self.speed
        elif direction == "down" and self.y + self.height < SCREEN_HEIGHT:
            self.y += self.speed



def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()