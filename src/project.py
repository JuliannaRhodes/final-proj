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

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

def add_ball(balls, timer):
    # Check if the current time has exceeded the timer
    if pygame.time.get_ticks() > timer:
        dx = random.choice([-3, 3])  # Random horizontal direction
        dy = random.choice([-3, 3])  # Random vertical direction
        new_ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, dx, dy, 10, (255, 255, 255))
        balls.append(new_ball)
        timer += 15000  # Add 15 seconds (15000 ms) to the timer
    return timer

def main():
    pygame.init()

    # Initialize screen and clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pongz")
    clock = pygame.time.Clock()

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Initialize objects
    left_paddle = Paddle(50, SCREEN_HEIGHT // 2 - 60, 10, 120, WHITE)
    right_paddle = Paddle(SCREEN_WIDTH - 60, SCREEN_HEIGHT // 2 - 60, 10, 120, WHITE)
    balls = [Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 3, 3, 10, WHITE)]

    # Initialize scores
    left_score = 0
    right_score = 0

    # Timer for adding balls
    ball_timer = pygame.time.get_ticks() + 5000

    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False






if __name__ == "__main__":
    main()