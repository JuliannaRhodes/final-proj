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
    player_paddle = Paddle(50, SCREEN_HEIGHT // 2 - 60, 10, 120, WHITE)
    balls = [Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 3, 3, 10, WHITE)]

    # Initialize score
    score = 0  # Player starts with 0 points

    # Timer for adding balls
    ball_timer = pygame.time.get_ticks() + 15000

    # Sound effects
    hit_sound = pygame.mixer.Sound("sounds/hit.wav")
    score_sound = pygame.mixer.Sound("sounds/score.wav")

    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_paddle.move("up")
        if keys[pygame.K_s]:
            player_paddle.move("down")

        # Ball movement and collision
        for ball in balls:
            ball.move()
            ball.draw(screen)

        # Collision with player paddle
            if (
                ball.x - ball.radius < player_paddle.x + player_paddle.width
                and player_paddle.y < ball.y < player_paddle.y + player_paddle.height
            ):
                ball.dx *= -1
                score += 1  # Increment score for a successful paddle hit
                score_sound.play()

        # Collision with the right wall
            if ball.x + ball.radius > SCREEN_WIDTH:
                ball.dx *= -1
        
        # Lose condition - Ball escapes past the player
            if ball.x < 0:
                hit_sound.play()  # Play hit sound
                running = False  # End the game
                break

        # Add a new ball every 15 seconds
        ball_timer = add_ball(balls, ball_timer)

        # Draw paddle and score
        player_paddle.draw(screen)
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (20, 20))

        # Game over message
        if not running:
            game_over_text = font.render("Game Over!", True, WHITE)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(3000)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

        

if __name__ == "__main__":
    main()