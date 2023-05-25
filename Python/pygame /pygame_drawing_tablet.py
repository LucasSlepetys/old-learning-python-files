import pygame, sys

WIDTH = 1300
HEIGHT = 750
#Colors
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
PINK = (255,0,127)
ORANGE = (255,153,51)
WHITE = (255,255,255)

draw = False
draw_line = False
task = None
color = BLACK
radius = 5
FPS = 1000
previus_point = None
last_pos = None
#Funtions:

def save():
    pass

def restart():
    game_window.fill(WHITE)
    screen_layout()

def fill():
    pass

def roundline(screen, color, start, end, radius):
    distance_x = end[0] - start[0]
    distance_y = end[1] - start[1]
    distance = max(abs(distance_x), abs(distance_y))
    for i in range(distance):
        x = int(start[0]+float(i)/ distance*distance_x)
        y = int(start[1]+float(i)/distance*distance_y)
        pygame.draw.circle(screen, color, (x,y), radius)

def free_drawing(event):
    global draw
    global color
    global last_pos
    if task == "free_drawing" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        draw = True
    elif task == "free_drawing" and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        draw = False
        last_pos = None


    if draw == True:
        mousex, mousey = pygame.mouse.get_pos()
        if mousex > 202 and mousey < 598 and last_pos != None:
            mouse = pygame.mouse.get_pos()
            pygame.draw.circle(game_window, color, mouse, radius)
            roundline(game_window, color, mouse, last_pos, radius)
            screen_check_line()

        last_pos = pygame.mouse.get_pos()

    mousex, mousey = pygame.mouse.get_pos()
    if mousex <= 200 or mousey >= 600:
        screen_layout()



def circle():
    pass

def square():
    pass

def rectangle():
    pass

def line(event):
    global draw_line
    global previus_point
    mousex, mousey = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONUP and event.button == 3 and mousex > 202 and mousey < 598:
        click_pos = pygame.mouse.get_pos()
        if previus_point != None:
            pygame.draw.line(game_window, color, previus_point, click_pos, radius)
        previus_point = click_pos
        screen_check_line()

    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        draw_line = True
        previus_point = None

    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        draw_line = False
        previus_point = None

    if draw_line == True and mousex > 202 and mousey < 598:
        click_pos = pygame.mouse.get_pos()
        if previus_point != None:
            pygame.draw.line(game_window, color, previus_point, click_pos, radius)
        previus_point = click_pos
        screen_check_line()


pygame.init()

game_window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Tablet")

game_running = True
game_window.fill((255,255,255))

#texts:
font = pygame.font.SysFont("Tahoma", 60, True, False)
font_2 = pygame.font.SysFont("Tahoma", 45, True, False)
text_save = font.render("SAVE", True, BLACK)
text_restart = font.render("RESTART", True, BLACK)
text_fill = font.render("FILL", True, BLACK)
text_free = font_2.render("Free", True, BLACK)
text_drawing = font_2.render("Drawing", True, BLACK)
text_erase = font.render("Erase", True, BLACK)

#screen layout:
def screen_check_line():
    mousex, mousey = pygame.mouse.get_pos()
    if mousex <= 251 or mousey >= 549:
        pygame.draw.line(game_window, BLACK, (200, 0), (200,750), 4)
        pygame.draw.line(game_window, BLACK, (0, 600), (1300, 600), 4)
def screen_radius():
    radius_rect = pygame.Rect(209, 29, 250, 35)
    pygame.draw.rect(game_window, WHITE, radius_rect, 0)
    if color != RED:
        radius_text = font.render("Radius: " + str(radius), True, RED)
        game_window.blit(radius_text, (210, 30))
    elif color == RED:
        radius_text = font.render("Radius: " + str(radius), True, BLACK)
        game_window.blit(radius_text, (210, 30))
def screen_layout():
    global save_rect
    global restart_rect
    global fill_rect
    global free_drawing_rect
    global blue_rect
    global red_rect
    global yellow_rect
    global pink_rect
    global orange_rect
    global black_rect
    global ellipsis_rect
    global first_rect
    global second_rect
    global line_rect
    global erase_rect
    global radius_rect
    pygame.draw.line(game_window, BLACK, (200, 0), (200,750), 4)
    pygame.draw.line(game_window, BLACK, (0, 600), (1300, 600), 4)

    #screen text:
    game_window.blit(text_save, (267, 662))
    save_rect = pygame.Rect(230, 630, 200, 100)
    pygame.draw.rect(game_window, BLACK, save_rect, 6)

    game_window.blit(text_restart, (480, 662))
    restart_rect = pygame.Rect(460, 630, 250, 100)
    pygame.draw.rect(game_window, BLACK, restart_rect, 6)

    game_window.blit(text_fill, (771, 662))
    fill_rect = pygame.Rect(740, 630, 160, 100)
    pygame.draw.rect(game_window, BLACK, fill_rect, 6)

    game_window.blit(text_free, (30, 652))
    game_window.blit(text_drawing, (30, 685))
    free_drawing_rect = pygame.Rect(20, 630, 160, 100)
    pygame.draw.rect(game_window, BLACK, free_drawing_rect, 6)


    game_window.blit(text_erase, (1140, 667))
    erase_rect = pygame.Rect(1130, 630, 150, 100)
    pygame.draw.rect(game_window, BLACK, erase_rect, 6)
    #fill colors:

    blue_rect = pygame.Rect(930, 630, 50, 45)
    pygame.draw.rect(game_window, BLUE, blue_rect)

    red_rect = pygame.Rect(930, 685, 50, 45)
    pygame.draw.rect(game_window, RED, red_rect)

    yellow_rect = pygame.Rect(990, 630, 50, 45)
    pygame.draw.rect(game_window, YELLOW, yellow_rect)

    pink_rect = pygame.Rect(990, 685, 50, 45)
    pygame.draw.rect(game_window, PINK, pink_rect)

    orange_rect = pygame.Rect(1050, 630, 50, 45)
    pygame.draw.rect(game_window, ORANGE, orange_rect)

    black_rect = pygame.Rect(1050, 685, 50, 45)
    pygame.draw.rect(game_window, BLACK, black_rect)
    #Screen shapes:

    ellipsis_rect = pygame.Rect(30, 30, 140, 100)
    pygame.draw.ellipse(game_window, BLACK, ellipsis_rect, 6)

    first_rect = pygame.Rect(40, 165, 120, 120)
    pygame.draw.rect(game_window, BLACK, first_rect, 6)

    second_rect = pygame.Rect(40, 325, 120, 160)
    pygame.draw.rect(game_window, BLACK, second_rect, 6)

    line_rect = pygame.Rect(20, 520, 150, 50)
    pygame.draw.line(game_window, BLACK, (30, 545), (170, 545), 5)

    radius_rect = pygame.Rect(209, 29, 250, 35)
    pygame.draw.rect(game_window, WHITE, radius_rect, 0)

    if color != RED:
        radius_text = font.render("Radius: " + str(radius), True, RED)
        game_window.blit(radius_text, (210, 30))
    elif color == RED:
        radius_text = font.render("Radius: " + str(radius), True, BLACK)
        game_window.blit(radius_text, (210, 30))


clock = pygame.time.Clock()
screen_layout()
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if save_rect.collidepoint(pygame.mouse.get_pos()):
                save()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if restart_rect.collidepoint(pygame.mouse.get_pos()):
                restart()
                color = BLACK
                task = None

        if event.type == pygame.MOUSEBUTTONDOWN:
            if fill_rect.collidepoint(pygame.mouse.get_pos()):
                task = "fill"
                fill()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if free_drawing_rect.collidepoint(pygame.mouse.get_pos()):
                task = "free_drawing"
                color = BLACK
        if task == "free_drawing":
            free_drawing(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if ellipsis_rect.collidepoint(pygame.mouse.get_pos()):
                task = "circle"
                circle()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if first_rect.collidepoint(pygame.mouse.get_pos()):
                task = "square"
                square()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if second_rect.collidepoint(pygame.mouse.get_pos()):
                task = "rectangle"
                rectangle()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if line_rect.collidepoint(pygame.mouse.get_pos()):
                task = "line"
                color = BLACK
                previus_point = None
        if task == "line":
            line(event)
        if task != "line":
            previus_point = None
        #Colors:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if blue_rect.collidepoint(pygame.mouse.get_pos()):
                if color != WHITE:
                    color = BLUE

        if event.type == pygame.MOUSEBUTTONDOWN:
            if red_rect.collidepoint(pygame.mouse.get_pos()):
                if color != WHITE:
                    color = RED

        if event.type == pygame.MOUSEBUTTONDOWN:
            if yellow_rect.collidepoint(pygame.mouse.get_pos()):
                if color != WHITE:
                    color = YELLOW

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pink_rect.collidepoint(pygame.mouse.get_pos()):
                if color != WHITE:
                    color = PINK

        if event.type == pygame.MOUSEBUTTONDOWN:
            if orange_rect.collidepoint(pygame.mouse.get_pos()):
                if color != WHITE:
                    color = ORANGE

        if event.type == pygame.MOUSEBUTTONDOWN:
            if black_rect.collidepoint(pygame.mouse.get_pos()):
                if color != WHITE:
                    color = BLACK

        if event.type == pygame.MOUSEBUTTONDOWN:
            if erase_rect.collidepoint(pygame.mouse.get_pos()):
                color = WHITE
                task = "free_drawing"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                radius_rect = pygame.Rect(209, 29, 253, 35)
                pygame.draw.rect(game_window, WHITE, radius_rect, 0)
                radius = 5
                screen_radius()
            elif event.key == pygame.K_2:
                radius_rect = pygame.Rect(209, 29, 253, 35)
                pygame.draw.rect(game_window, WHITE, radius_rect, 0)
                radius = 10
                screen_radius()
            elif event.key == pygame.K_3:
                radius_rect = pygame.Rect(209, 29, 253, 35)
                pygame.draw.rect(game_window, WHITE, radius_rect, 0)
                radius = 15
                screen_radius()
            elif event.key == pygame.K_4:
                radius_rect = pygame.Rect(209, 29, 253, 35)
                pygame.draw.rect(game_window, WHITE, radius_rect, 0)
                radius = 20
                screen_radius()
            elif event.key == pygame.K_5:
                radius_rect = pygame.Rect(209, 29, 253, 35)
                pygame.draw.rect(game_window, WHITE, radius_rect, 0)
                radius = 25
                screen_radius()
            elif event.key == pygame.K_6:
                radius_rect = pygame.Rect(209, 29, 253, 35)
                pygame.draw.rect(game_window, WHITE, radius_rect, 0)
                radius = 30
                screen_radius()
            elif event.key == pygame.K_7:
                radius_rect = pygame.Rect(209, 29, 253, 35)
                pygame.draw.rect(game_window, WHITE, radius_rect, 0)
                radius = 35
                screen_radius()
            elif event.key == pygame.K_8:
                radius_rect = pygame.Rect(209, 29, 253, 35)
                pygame.draw.rect(game_window, WHITE, radius_rect, 0)
                radius = 40
                screen_radius()
            elif event.key == pygame.K_9:
                radius_rect = pygame.Rect(209, 29, 253, 35)
                pygame.draw.rect(game_window, WHITE, radius_rect, 0)
                radius = 50
                screen_radius()

        if radius_rect.collidepoint(pygame.mouse.get_pos()):
            screen_radius()
        mousex, mousey = pygame.mouse.get_pos()
        if mousex >= 200 and mousex <= 600 and mousey >= 0 and mousey <= 300:
            screen_radius()







    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
