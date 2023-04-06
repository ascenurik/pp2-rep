import random
import sys
import pygame
import time

pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0, 255)
WHITE = (255, 255, 255)
BROWN = (139, 69, 19, 255)
DARK_GREEN = (0, 100, 0, 255)
BLOCK_SIZE = 40
clock = pygame.time.Clock()
LEVEL = 1
SCORE = 0
font_small = pygame.font.SysFont("Verdana", 20)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Level:
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):

        pygame.draw.rect(screen, DARK_GREEN,
                         (self.location.x * BLOCK_SIZE, self.location.y * BLOCK_SIZE, 3 * BLOCK_SIZE, 5 * BLOCK_SIZE))

    def first(self, S, LEVEL):
        if LEVEL == 2:
            x = random.randint(1, WIDTH // BLOCK_SIZE - 2)
            y = random.randint(1, HEIGHT // BLOCK_SIZE - 2)
            if not any(part.x == x and part.y == y for part in S.body):
                self.location = Point(x, y)


class Snake:
    def __init__(self):
        self.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
        ]

    def draw_body(self):
        for body in self.body[1:]:
            pygame.draw.rect(screen, BLUE, (body.x * BLOCK_SIZE, body.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def draw_head(self):
        head = self.body[0]
        pygame.draw.rect(screen, RED, (head.x * BLOCK_SIZE, head.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def move(self, dx, dy, game_over, screen):
        # Get the current head position
        head = self.body[0]

        # Calculate the new head position
        new_head = Point(head.x + dx, head.y + dy)

        # Check if the new head position collides with the body
        if any(part.x == new_head.x and part.y == new_head.y for part in self.body[1:]):
            white_surface = pygame.Surface((WIDTH, HEIGHT))
            white_surface.fill(WHITE)
            screen.blit(white_surface, (0, 0))
            screen.blit(game_over, (160, 400))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            sys.exit()

        # Move the body parts
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y

        # Move the head to the new position
        self.body[0] = new_head

        # Apply the border constraints
        self.border()

    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False

        return True

    def border(self):
        if self.body[0].x > WIDTH // BLOCK_SIZE:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // BLOCK_SIZE
        elif self.body[0].y < 0:
            self.body[0].y = WIDTH // BLOCK_SIZE
        elif self.body[0].y > HEIGHT // BLOCK_SIZE:
            self.body[0].y = 0


def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)


class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):
        pygame.draw.rect(screen, GREEN,
                         (self.location.x * BLOCK_SIZE, self.location.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def generator(self, S):
        while True:
            x = random.randint(1, WIDTH // BLOCK_SIZE - 2)
            y = random.randint(1, HEIGHT // BLOCK_SIZE - 2)
            if not any(part.x == x and part.y == y for part in S.body):
                self.location = Point(x, y)
                break


def main():
    done = False
    S = Snake()
    F = Food(5, 5)
    L = Level(10, 10)
    dx, dy = 0, -1
    ok = True
    FPS = 5
    check = True
    direction = 'up'
    font = pygame.font.SysFont("Verdana", 90)
    game_over = font.render("Game Over", True, BLACK)
    while not done:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP and direction != 'down':
                    dx, dy = 0, -1
                    direction = 'up'
                elif event.key == pygame.K_DOWN and direction != 'up':
                    dx, dy = 0, +1
                    direction = 'down'
                elif event.key == pygame.K_RIGHT and direction != 'left':
                    dx, dy = 1, 0
                    direction = 'right'
                elif event.key == pygame.K_LEFT and direction != 'right':
                    dx, dy = -1, 0
                    direction = 'left'

        S.move(dx, dy, game_over, screen)

        if S.check_collision(F):
            global SCORE, LEVEL
            SCORE += 1
            if SCORE % 5 == 0 and SCORE != 0:
                LEVEL += 1
                ok = True

            S.body.append(
                Point(S.body[1].x, S.body[1].y)
            )
            F.generator(S)

        if LEVEL > 1 and ok == True:
            FPS += 2
            ok = False

        score = font_small.render(str(SCORE), True, RED)
        level = font_small.render(str(LEVEL), True, YELLOW)
        screen.blit(score, (10, 10))
        screen.blit(level, (780, 10))

        S.draw_head()
        S.draw_body()
        if LEVEL > 1:
            L.draw()
        F.draw()

        draw_grid()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()