import pygame, sys

WIDTH = 600
HEIGHT = 400

pygame.init()

game_window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testing what I know")

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("w")
            elif event.key == pygame.K_x:
                print("x")
            elif event.key == pygame.K_a:
                print("a")

    game_window.fill((0,0,0))
    pygame.display.update()

pygame.quit()
sys.exit()
