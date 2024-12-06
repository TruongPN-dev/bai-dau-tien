from datetime import datetime
import pygame
def thoi_gian():
    global font
    current_time = datetime.now().strftime("%H:%M:%S")
    text_time = font_time.render(current_time, True, red)
    text_time_rec = text_time.get_rect(center=(770,260))

    current_date = datetime.now().strftime(r"%A-%d/%m/%Y")
    text_date = font_date.render(current_date, True, green)
    text_date_rec = text_date.get_rect(center=(770,500))
    screen.fill(black)
    screen.blit(text_time,text_time_rec)
    screen.blit(text_date,text_date_rec)
pygame.init()
screen = pygame.display.set_mode((1540,840))
#2 dòng này sẽ cho phép pygame tạo fullscreen
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# screen_width, screen_height = pygame.display.get_surface().get_size()
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
white = (255,255,255)
font_time = pygame.font.Font(r'C:\Windows\Fonts\LCDM2B__.TTF', 200)
font_date = pygame.font.Font(r'C:\Windows\Fonts\IMPRISHA.TTF', 150)
clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    thoi_gian()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()