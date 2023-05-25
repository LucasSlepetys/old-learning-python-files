import pygame

pygame.init()

#Variables
BLACK = (0,0,0,)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)


game = True
clock = pygame.time.Clock()

#Open new window
size = (696, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

#Main program loop
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, [0, 0, 696, 2], 5)
    pygame.draw.rect(screen, BLACK, [0, 498, 696, 2], 5)

    pygame.draw.rect(screen, BLACK, [0, 0, 2, 696], 5)
    pygame.draw.rect(screen, BLACK, [694, 0, 2, 696], 5)


    pygame.draw.rect(screen, GREEN, [2, 2, 112, 494], 0)
    pygame.draw.rect(screen, RED, [118, 2, 112, 494], 0)
    pygame.draw.rect(screen, RED, [234, 2, 112, 494], 0)
    pygame.draw.rect(screen, RED, [350, 2, 112, 494], 0)
    pygame.draw.rect(screen, RED, [466, 2, 112, 494], 0)
    pygame.draw.rect(screen, GREEN, [582, 2, 112, 494], 0)
    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # pygame.draw.ellipse(screen, BLACK, [20, 20, 255, 100], 2)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
