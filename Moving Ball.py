import pygame
pygame.init()
pygame.display.set_caption("Moving Ball")

WIDTH = 510
HEIGHT = 510
FPS = 60

x = 25
y = 25

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
screen.fill((255, 255, 255))
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > 25: y -= 20
    if pressed[pygame.K_DOWN] and y < HEIGHT - 25: y += 20
    if pressed[pygame.K_LEFT] and x > 25: x -= 20
    if pressed[pygame.K_RIGHT] and x < WIDTH - 25: x += 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pygame.display.flip()

pygame.quit()