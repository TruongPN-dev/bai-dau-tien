#hai cau lenh bat buoc phai co khi lap trinh game
import pygame, sys
# import time
pygame.init() #khoi tao game
p = 2 #khoi tao trọng lực cho bird
bird_y = 300 #khoi tao chim bay len
diem = 0
game_play = True
running = True
loop = True
roi = True
hight_score = 0
floor_x = 0 #lam cho san di chuyen
pygame.display.set_caption('Game bird') #dat tieu de cho game
icon = pygame.image.load(r'D:\Python\FileGame\assets\yellowbird-downflap.png')#tao icon, 'r' de k anh huong toi \ trong duong link
pygame.display.set_icon(icon)
background = pygame.image.load(r'D:\Python\FileGame\assets\background-night.png')#tao hinh nen game
background = pygame.transform.scale2x(background)#phong to hinh nen cho vua mang hinh game
floor = pygame.image.load(r'D:\Python\FileGame\assets\floor.png')
floor = pygame.transform.scale2x(floor)
bird = pygame.image.load(r'D:\Python\FileGame\assets\yellowbird-downflap.png')
bird = pygame.transform.scale2x(bird)
game_over = pygame.image.load(r'D:\Python\FileGame\assets\message.png')
game_over = pygame.transform.scale2x(game_over)
game_over_rect = game_over.get_rect(center = (216,320))
font = pygame.font.Font(r'D:\Python\FileGame\04B_19.TTF', 45) #dua font chu va kich thuoc chu
def diem_so():
	if game_play:
		diem_f = font.render(str(int(diem)), True, (255,255,255))
		diem_rect = diem_f.get_rect(center = (216,80))
		screen.blit(diem_f, diem_rect)
	if game_play == False:
		diem_f = font.render(f'Score: {int(diem)}', True, (255,255,255))
		diem_rect = diem_f.get_rect(center = (216,60))
		screen.blit(diem_f, diem_rect)
		diem_h_f = font.render(f'Hight Score: {int(hight_score)}', True, (255,255,255))
		diem_h_rect = diem_h_f.get_rect(center = (216,560))
		screen.blit(diem_h_f, diem_h_rect)
def va_cham():
	if bird_y > 557 or bird_y < -1:
		return False
	else:
		return True
#cua so game
screen = pygame.display.set_mode((432,768))
while loop:
	bird_rect = bird.get_rect(center = (53, bird_y))
	screen.blit(background, (0,0))
	screen.blit(floor, (0,600))
	screen.blit(bird, bird_rect)
	pygame.display.update()#update hinh nen
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			loop = False
			sys.exit()
		if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and game_play:
					while running:
						bird_rect = bird.get_rect(center = (53, bird_y))
						for event in pygame.event.get(): #event la nhung thao tac tren mang hinh game
							if event.type == pygame.QUIT:
								running = False
								loop = False
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_SPACE and game_play:
									bird_y = bird_y - 100
								if event.key == pygame.K_SPACE and game_play == False:
									game_play = True
									bird_y = 300
									diem = 0
						screen.blit(background,(0,0))#dua hinh nen vao nhung se chua hien thi =>can phai update
						floor_x-=1 #giong voi floor_x = floor_x - 1
						screen.blit(floor,(floor_x,600))
						if floor_x == -240:
							floor_x = 0
						if game_play:
							screen.blit(bird, bird_rect)
							bird_y = bird_y + p
							diem_so()
							diem+=0.5
							game_play = va_cham() 
						else:
							screen.blit(game_over, game_over_rect)
							diem_so()
						if diem > hight_score:
								hight_score = diem
						pygame.display.update()#update hinh nen