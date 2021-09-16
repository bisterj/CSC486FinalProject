import pygame
import random
import time
import sys

cookie = pygame.image.load("cookie.png")
pog = pygame.image.load("pog2.png")
# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')

# window size
frame_x = 600
frame_y = 400

# Window for the game
pygame.display.set_caption("Taylor's adventure to find the Cookies of Knowledge")
window = pygame.display.set_mode((frame_x, frame_y))

# colors
# TODO put in colors for game
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

# TODO fps controller??
fps_controller = pygame.time.Clock()

# game variables
tay_pos = [20, 20]
# TODO body?

cookie_pos = [random.randrange(1, frame_x // 20) * 20, random.randrange(1, frame_y // 20) * 20]
cookie_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

# GAME OVER
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_x/2, frame_y/4)
    window.fill(black)
    window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_x / 10, 15)
    else:
        score_rect.midtop = (frame_x / 2, frame_y / 1.25)
    window.blit(score_surface, score_rect)


# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.quit))

        # Making sure the snake cannot move in the opposite direction instantaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        tay_pos[1] -= 20
    if direction == 'DOWN':
        tay_pos[1] += 20
    if direction == 'LEFT':
        tay_pos[0] -= 20
    if direction == 'RIGHT':
        tay_pos[0] += 20

    # spawn cookies
    if not cookie_spawn:
        cookie_pos = [random.randrange(1, frame_x // 20) * 20, random.randrange(1, frame_y // 20) * 20]
    cookie_spawn = True

    # drawing in the game
    window.fill(black)
    # pygame.draw.rect(window, green, pygame.Rect(tay_pos[0], tay_pos[1], 20, 20))
    window.blit(pog, (tay_pos[0], tay_pos[1]))

    if cookie_spawn:
        # pygame.draw.rect(window, white, pygame.Rect(cookie_pos[0], cookie_pos[1], 20, 20))
        window.blit(cookie, (cookie_pos[0], cookie_pos[1]))

    if tay_pos[0] < 0 or tay_pos[0] > frame_x - 20:
        game_over()
    if tay_pos[1] < 0 or tay_pos[1] > frame_y - 20:
        game_over()

    if tay_pos == cookie_pos:
        score += 1
        cookie_spawn = False

    show_score(1, white, "consolas", 20)

    pygame.display.update()

    fps_controller.tick(10)