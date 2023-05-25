import pygame, sys
WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 750
BLACK = (0,0,0)
color = BLACK
draw = False
task = None
radius = 10
FPS = 120
mousex = 0
mousey = 0
pygame.init()

#Create game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()
pygame.display.set_caption("Learning pygame")
game_window.fill((255,255,255))
game_running = True
while game_running:
    #look throught all active events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                task = "free_drawing"

            elif event.key == pygame.K_a:
                task = None


        if task == "free_drawing" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            draw = True
        elif task == "free_drawing" and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            draw = False

    if draw == True:
        mousex, mousey = pygame.mouse.get_pos()
        if mousex > 0 and mousey < 750 and color == BLACK:
            mouse = pygame.mouse.get_pos()
            pygame.draw.circle(game_window, color, event.pos, radius)
            pygame.display.flip()



    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
