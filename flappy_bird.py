import pygame, sys, random
from random import randint
def draw_floor():
    screen.blit(floor,(floor_x,650))
    screen.blit(floor,(floor_x+432,650))
def create_pipe():
    random_pipe_pos = random.randint(150,600)
    bottom_pipe = pipe_surface.get_rect(midtop = (500, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop = (500, random_pipe_pos-700))
    return bottom_pipe, top_pipe
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 2
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:    
            screen.blit(pipe_surface, pipe) 
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)
def va_cham(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
    if bird_rect.top <= 0 or bird_rect.bottom >= 650:
            return False
    return True
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1,-bird_move*3,1)
    return new_bird
def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
    return new_bird, new_bird_rect
def score_display(game_state):
    if game_state == "main_game":
        score_serface = game_font.render(str(int(score)), True, (255,255,255))
        score_rect = score_serface.get_rect(center=(216,100))
        screen.blit(score_serface,score_rect)
    if game_state == "game_over":
        score_serface = game_font.render(f"Score: {int(score)}", True, (255,255,255))
        score_rect = score_serface.get_rect(center=(216,100))
        screen.blit(score_serface,score_rect)

        high_score_serface = game_font.render(f"High Score: {int(high_score)}", True, (255,255,255))
        high_score_rect = high_score_serface.get_rect(center=(216,630))
        screen.blit(high_score_serface,high_score_rect)
def update_score(score,high_score):
    if score > high_score:
        high_score = score
    return high_score
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)#chỉnh âm thanh chuẩn xác theo chuyển động
pygame.init()
gravity = 0.25
bird_move = 0
floor_x = 0
score = 0
high_score = 0
game_active = True
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
bg  = pygame.transform.scale2x(pygame.image.load(r'D:\Python\FileGame\assets\background-night.png')).convert()
floor = pygame.transform.scale2x(pygame.image.load(r'D:\Python\FileGame\assets\floor.png')).convert()
bird_up = pygame.transform.scale2x(pygame.image.load(r'D:\Python\FileGame\assets\yellowbird-upflap.png')).convert_alpha()
bird_mid = pygame.transform.scale2x(pygame.image.load(r'D:\Python\FileGame\assets\yellowbird-midflap.png')).convert_alpha()
bird_down = pygame.transform.scale2x(pygame.image.load(r'D:\Python\FileGame\assets\yellowbird-downflap.png')).convert_alpha()
gameover_surface = pygame.transform.scale2x(pygame.image.load(r'D:\Python\FileGame\assets\message.png')).convert_alpha()
flap_sound = pygame.mixer.Sound(r"D:\Python\FileGame\sound\sfx_wing.wav")
hit_sound = pygame.mixer.Sound(r"D:\Python\FileGame\sound\sfx_hit.wav")
score_sound = pygame.mixer.Sound(r"D:\Python\FileGame\sound\sfx_point.wav")
score_sound_countdown = 100
gameover_rect = gameover_surface.get_rect(center=(216,384))
game_font = pygame.font.Font(r'D:\Python\FileGame\04B_19.TTF', 45)
bird_list = [bird_down, bird_mid, bird_up]
bird_index = 0
bird = bird_list[bird_index]
bird_rect = bird.get_rect(center = (100,384))
birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap,200)
pipe_surface = pygame.image.load(r'D:\Python\FileGame\assets\pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
spawpipe = pygame.USEREVENT#tao ong xuat hien
pygame.time.set_timer(spawpipe, 2000)#ống suất hiện mỗi 2s
# pipe_height = [100,200,300,400]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_move = 0
                bird_move = -5.5
                flap_sound.play()  
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100,384)
                bird_move = 0
                score = 0
        if event.type == spawpipe:
            pipe_list.extend(create_pipe())
        if event.type == birdflap:  
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird, bird_rect = bird_animation()
    screen.blit(bg,(0,0))
    if game_active:
        bird_move += gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_move
        screen.blit(rotated_bird,bird_rect)
        game_active = va_cham(pipe_list)
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        score += 0.009
        score_display("main_game")
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(gameover_surface,gameover_rect)
        score_display("game_over")
        high_score = update_score(score,high_score)
    floor_x -= 1
    draw_floor()
    if floor_x <= -432:
        floor_x = 0
    pygame.display.update()
    clock.tick(120)#fps của game