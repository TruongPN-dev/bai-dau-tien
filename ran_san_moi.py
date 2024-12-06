import pygame
import random
import sys
from time import sleep
#khởi tạo game
pygame.init()
#khai báo các biến trong game
running = True
x = 100
y = 100
move = "right"
#khai báo màu sắc
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
grey = (211,211,211)
black = (0, 0, 0)
#tạo màn hình game
screen = pygame.display.set_mode((800,800))
#đặt tiêu đề game
pygame.display.set_caption('Rắn săn mồi')
#vẽ rắn
def ran():
    snake = pygame.draw.rect(screen, green, (x,y,30,30))
#vẽ food
def moi():
    # pygame.draw.rect(screen, red, (random.randint(0,800),random.randint(0,800),30,30))
    food = pygame.draw.rect(screen, red, (100,300,30,30))
while running:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move = "left"
            if event.key == pygame.K_RIGHT:
                move = "right"
            if event.key == pygame.K_DOWN:
                move = "down"
            if event.key == pygame.K_UP:
                move = "up"
    if move == "right":
        x += 0.3
        if x > 800:
            x = 0
    elif move == "left":
        x -= 0.3
        if x < 0:
            x = 800
    elif move == "up":
        y -= 0.3
        if y < 0:
            y = 800
    elif move == "down":
        y += 0.3
        if y > 800:
            y = 0
        running = False
    ran()
    moi()
    pygame.display.update()