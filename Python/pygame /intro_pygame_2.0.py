import pygame, sys, random, time

#! Functions

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,450))
    screen.blit(floor_surface,(floor_x_pos + 288,450))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (350,random_pipe_pos))
    top_pipe  = pipe_surface.get_rect(midbottom = (350,random_pipe_pos - 150))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 6
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= -50 or bird_rect.bottom >= 450:
        return False

    return True

def score_display(game_state):
    if game_state == "main_game":
        score_surface = game_font.render(str(int(score)), True, (255,255,255))
        score_rect = score_surface.get_rect(center = (144,50))
        screen.blit(score_surface, score_rect)
    if game_state == "game_over":
        high_score_surface = game_font.render(f'Score: {int(score)}', True, (255,255,255))
        high_score_rect = high_score_surface.get_rect(center = (144,50))
        screen.blit(high_score_surface, high_score_rect)

        score_surface = game_font.render(f'High Score: {int(high_score)}', True, (255,255,255))
        score_rect = score_surface.get_rect(center = (144,425))
        screen.blit(score_surface, score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird
#! ----------------

pygame.init()
screen = pygame.display.set_mode((288,512))
#FPS
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf',40)

#! Game variables
gravity = 0.8
bird_movement = 0
game_active = True
score = -1
high_score = 0


# Import image #* Scale image by 2
bg_surface = pygame.image.load('assets/background-day.png').convert()

floor_surface = pygame.image.load('assets/base.png').convert()
floor_x_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
# Put rectancle around surgace
bird_rect = bird_surface.get_rect(center = (50,256))

pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [200, 300, 400]

gameover_surface = pygame.image.load('assets/gameover.png').convert()
gameover_rect = gameover_surface.get_rect(center = (140,256))


#! Loop to update screen
while True:
    # Check if button is clicked and then runs code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 10
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (50,256)
                bird_movement = 0
                score = -0.35




        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())


    # Display surfaces
    screen.blit(bg_surface, (0,0))


    if game_active:
        # Bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)
        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # Change image
        if bird_movement <= 0:
            bird_surface = pygame.image.load('assets/bluebird-downflap.png').convert_alpha()

        else:
            bird_surface = pygame.image.load('assets/bluebird-upflap.png').convert_alpha()

        score += 0.025
        score_display("main_game")
    else:
        high_score = update_score(score, high_score)
        score_display("game_over")
        screen.blit(gameover_surface, gameover_rect)



    # Floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -288:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
