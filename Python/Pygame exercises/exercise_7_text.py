import pygame, sys
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

pygame.init()

#Create game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Learning pygame")

game_running = True
# font = pygame.font.SysFont("Tahoma", 60, True, False)
font = pygame.font.Font("Roboto-Bold.ttf", 48)
text = font.render("Hello world", True, (0,0,0))
while game_running:
    #look throught all active events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    game_window.fill((255,255,255))
    game_window.blit(text, (100,100))

    pygame.display.update()

pygame.quit()
sys.exit()
