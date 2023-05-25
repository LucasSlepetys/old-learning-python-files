import pygame, sys
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

pygame.init()

#Create game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Learning pygame")

game_running = True
while game_running:
    #look throught all active events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        #Control character movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("Move the character forwards")
            elif event.key == pygame.K_s:
                print("Move the character backwards")
            elif event.key == pygame.K_a:
                print("Move the character left")
            elif event.key == pygame.K_d:
                print("Move the character right")

    game_window.fill((255,255,255))

    pygame.display.update()

pygame.quit()
sys.exit()
