import pygame, sys, random
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

pygame.init()

#Functions
def process_click(event):
    global previous_point
    click_pos = event.pos
    if previous_point != None:
        pygame.draw.line(game_window, (RED,GREEN,BLUE), previous_point, click_pos, 5)
    previous_point = click_pos

#Create game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Learning pygame")

game_running = True
game_window.fill((255,255,255))
previous_point = None
while game_running:
    #look throught all active events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            RED = random.randint(0,255)
            GREEN = random.randint(0,255)
            BLUE = random.randint(0,255)
            process_click(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                game_window.fill((255,255,255))
                previous_point = None




    pygame.display.update()

pygame.quit()
sys.exit()
