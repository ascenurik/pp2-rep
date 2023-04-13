import pygame, sys
import random, time

pygame.init()

FPS = 60
clock = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

MY_SPEED = 5
ENEMY_SPEED = 5
SCORE = 0
GAME_LEVEL = "Easy"
coin_counter = 0

font_small = pygame.font.SysFont("Verdana", 20)
font_ = pygame.font.SysFont("comicsansms", 20)

font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

screen = pygame.display.set_mode((400, 600))
screen.fill(WHITE)
pygame.display.set_caption("Racer Game")

tenge_img = pygame.transform.scale(pygame.image.load('Coin1.png'), (50, 50))
dollar_img = pygame.transform.scale(pygame.image.load('Coin2.png'), (50, 50))
euro_img = pygame.transform.scale(pygame.image.load('Coin3.png'), (50, 50))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, ENEMY_SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -MY_SPEED)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, MY_SPEED)

        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-MY_SPEED, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(MY_SPEED, 0)


class EuroCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = euro_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 250), random.randint(0, 100))

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(50, SCREEN_WIDTH - 250), random.randint(0, 100))

    def appear(self):
        self.rect.top = 0
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 250), random.randint(0, 100))


class DollarCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = dollar_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(SCREEN_WIDTH - 250, SCREEN_WIDTH - 150), random.randint(0, 100))

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(SCREEN_WIDTH - 250, SCREEN_WIDTH - 150), random.randint(0, 100))

    def appear(self):
        self.rect.top = 0
        self.rect.center = (random.randint(SCREEN_WIDTH - 250, SCREEN_WIDTH - 150), random.randint(0, 100))


class TengeCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = tenge_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(SCREEN_WIDTH - 150, SCREEN_WIDTH - 50), random.randint(0, 100))

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(SCREEN_WIDTH - 150, SCREEN_WIDTH - 50), random.randint(0, 100))

    def appear(self):
        self.rect.top = 0
        self.rect.center = (random.randint(SCREEN_WIDTH - 150, SCREEN_WIDTH - 50), random.randint(0, 100))


p1 = Player()
e1 = Enemy()
c_euro = EuroCoin()
c_dollar = DollarCoin()
c_tenge = TengeCoin()

enemies = pygame.sprite.Group()
player = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

enemies.add(e1)
player.add(p1)
coins.add(c_euro)
coins.add(c_dollar)
coins.add(c_tenge)

all_sprites.add(e1)
all_sprites.add(p1)
all_sprites.add(c_euro)
all_sprites.add(c_dollar)
all_sprites.add(c_tenge)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
                                         event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))

    for_SCORES = font_small.render("Score: " + str(SCORE), True, BLACK)
    screen.blit(for_SCORES, (10, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(p1, enemies):
        time.sleep(0.5)

        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        txt = font_.render(f"Coins: {coin_counter} || Score: {SCORE} || Level: {GAME_LEVEL}", True, BLACK)
        screen.blit(txt, (15, 350))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(c_euro, player):
        coin_counter += 5
        c_euro.appear()

    if pygame.sprite.spritecollideany(c_euro, enemies):
        c_euro.appear()

    if pygame.sprite.spritecollideany(c_dollar, player):
        coin_counter += 3
        c_dollar.appear()

    if pygame.sprite.spritecollideany(c_dollar, enemies):
        c_dollar.appear()

    if pygame.sprite.spritecollideany(c_tenge, player):
        coin_counter += 1
        c_tenge.appear()

    if pygame.sprite.spritecollideany(c_tenge, enemies):
        c_tenge.appear()

    if coin_counter >= 30 and coin_counter < 50:
        GAME_LEVEL = "Medium"
        ENEMY_SPEED = 10
        MY_SPEED = 8
    if coin_counter >= 50:
        GAME_LEVEL = "Hard"
        ENEMY_SPEED = 15
        MY_SPEED = 10

    font_for_COINS = font_small.render(f"Coins: {coin_counter}", True, BLACK)
    screen.blit(font_for_COINS, (250, 10))

    font_for_COINS = font_small.render(f"Level: {GAME_LEVEL}", True, BLACK)
    screen.blit(font_for_COINS, (250, 30))

    font_for_COINS = font_small.render(f"My Speed: {round(MY_SPEED)}", True, BLACK)
    screen.blit(font_for_COINS, (10, 30))

    font_for_COINS = font_small.render(f"Enemy Speed: {round(ENEMY_SPEED)}", True, BLACK)
    screen.blit(font_for_COINS, (10, 50))

    pygame.display.update()
    clock.tick(FPS)
