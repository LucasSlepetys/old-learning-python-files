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


    game_window.fill((255,255,255))
    filled_rect = pygame.Rect(100,100,25,25)
    pygame.draw.rect(game_window, (0,0,0), filled_rect)

    empty_rect = pygame.Rect(200, 200, 25, 25)
    pygame.draw.rect(game_window, (255,0,0), empty_rect, 3)

#---------------------------------------------------------------------------

    points = [(150, 150), (200,120), (210, 150), (260, 140), (210, 250)]
    pygame.draw.polygon(game_window, (0,0,0), points)

    points = [(350, 350), (400, 320), (460, 340), (410, 450)]
    pygame.draw.polygon(game_window, (0,0,255), points, 4)

#---------------------------------------------------------------------------

    pygame.draw.circle(game_window, (255,0,0), (250,250), 50)


    ellipsis_rect = pygame.Rect(500, 400, 200, 100)
    pygame.draw.ellipse(game_window, (255,0,255), ellipsis_rect)

#---------------------------------------------------------------------------

    pygame.draw.line(game_window, (255,0,0), (100,100), (300,200), 5)


    pygame.display.update()

pygame.quit()
sys.exit()
