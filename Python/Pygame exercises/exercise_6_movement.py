import pygame, sys
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
RECT_WIDTH = 150
RECT_HEIGHT = 150
FPS = 120

x_pos = WINDOW_WIDTH / 2 - RECT_WIDTH / 2
y_pos = WINDOW_HEIGHT / 2 - RECT_HEIGHT / 2

# x_pos = 100
# y_pos = 100

x_vel = 0
y_vel = 0

pygame.init()

print("x_pos = ", x_pos)
print("y_pos = ", y_pos)

print("x_vel = ", x_vel)
print("y_vel = ", y_vel)
#Create game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Learning pygame")
clock = pygame.time.Clock()

game_running = True
while game_running:
    #look throught all active events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        #Control character movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_vel += 5
            if event.key == pygame.K_LEFT:
                x_vel -= 5
            if event.key == pygame.K_UP:
                y_vel -= 5
            if event.key == pygame.K_DOWN:
                y_vel += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_vel -= 5
            if event.key == pygame.K_LEFT:
                x_vel += 5
            if event.key == pygame.K_UP:
                y_vel += 5
            if event.key == pygame.K_DOWN:
                y_vel -= 5


    game_window.fill((255,255,255))

    x_pos += x_vel
    y_pos += y_vel

    rect = pygame.Rect(x_pos, y_pos, RECT_WIDTH, RECT_HEIGHT)
    pygame.draw.rect(game_window, (255, 0, 0), rect)


    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
