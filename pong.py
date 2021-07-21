# Importing the library
import pygame,random, time
  
# Initializing Pygame
pygame.init()
 
#Window size
WIDTH,HEIGHT = 700,800
# Initializing surface
win = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Pong")
  
# Initialing RED
RED = (255,0,0)
BLUE_LIGHT = (52, 232, 235)
WHITE = (255,255,255)
  
run = True
x1=100
x2 = 700
y1 =350
y2 = 350
x3 =400
y3 = 400

player_score = 0
opponent_score = 0

clock = pygame.time.Clock()


player =  pygame.Rect(50,250,10,100 )
opponent = pygame.Rect(650,250,10,100)
ball = pygame.Rect(290,310,20,20)
line = pygame.Rect(0,700,700,5)

myfont = pygame.font.SysFont('Times New Roman', 30)




ball_speed_x = 2 * random.choice((1,-1))
ball_speed_y = 2 * random.choice((1,-1))

def ball_restart():
	time.sleep(1)
	ball.center =(400,400)
	ball_speed_x = random.choice((1,-1))
	ball_speed_y = random.choice((1,-1))




while run:
	


	
	key = pygame.key.get_pressed()
	#spped of ball
	ball.x += ball_speed_x 
	ball.y += ball_speed_y

 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	if key[pygame.K_DOWN] and player.y  + 100< 680:
		player.y += 8

	if key[pygame.K_UP] and player.y >10:
		player.y -= 8
	if key[pygame.K_s] and opponent.y +100 < 680:
		opponent.y += 8

	if key[pygame.K_w] and opponent.y>10 :
		opponent.y -= 8

	if ball.top <=0 or ball.bottom >= 700:
		ball_speed_y *= -1

	if ball.left <=0 or ball.right >= 700:
		if ball.left <=0:
			opponent_score += 1
		if ball.right>=700:
			player_score += 1

		ball_restart()
	

	if ball.colliderect(player) or ball.colliderect(opponent):
		ball_speed_x *= -1
		

	if ball.left<= 0 or ball.right>= 800:
		pygame.Rect(410,400,20,20)


	
	win.fill(1)
	pygame.draw.rect(win,RED,player)
	pygame.draw.rect(win,RED,opponent)
	pygame.draw.rect(win,BLUE_LIGHT,ball)
	pygame.draw.rect(win,WHITE,line)
	
	textsurface = myfont.render(f"                   Player_A: {player_score}      Player_B: {opponent_score}" , False, (255, 255, 255))
	win.blit(textsurface,(0,715))
	pygame.display.flip()
	clock.tick(60)
		



pygame.quit()