import pygame
import os
import time
import random
pygame.font.init()

RED_SPACEplayer= pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACEplayer= pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACEplayer= pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
YELLOW_SPACEplayer= pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

RED_LASERS= pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASERS= pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASERS= pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASERS= pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

WIDTH, HEIGHT= 750,750
BG= pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


WIN= pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space Shooter")


class player: #i create a class for both enemy and ally players with stuff
	def __init__(self, x,y,health=100):
		self.x=x
		self.y=y
		self.health=health
		self.player_img=None
		self.laser_img=None
		self.lasers=[]
		self.cool_down_counter=0

	def draw(self,window):
		window.blit(self.player_img, (self.x, self.y))

class Player(player):
	def __init__(self, x, y, health=100):
		super().__init__(x,y,health)
		self.player_img= YELLOW_SPACEplayer
		self.laser_img= YELLOW_LASERS
		self.mask= pygame.mask.from_surface(self.player_img)
		self.max_health=health




def main():
	run=True
	FPS=60
	level=1
	lives=5
	main_font= pygame.font.SysFont("comicsans", 50)
	player_vel=5
	player=Player(300,650)

	clock=pygame.time.Clock()

	def redraw_window():
		WIN.blit(BG, (0,0))
		lives_label= main_font.render("lives: " + str(lives), 1, (255,255,255))
		level_label= main_font.render("level: " + str(level), 1, (255,255,255))

		WIN.blit(lives_label, (10,10))
		WIN.blit(level_label, (WIDTH - level_label.get_width()-10,10))
		
		player.draw(WIN)

		pygame.display.update()
	



	while run:
		clock.tick(FPS)
		redraw_window()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run=False

		keys=pygame.key.get_pressed()
		if keys[pygame.K_a] and player.x - player_vel >0:
			player.x -= player_vel
		if keys[pygame.K_d] and player.x + player_vel + 50 <WIDTH:
			player.x += player_vel
		if keys[pygame.K_w] and player.y - player_vel >0:
			player.y -= player_vel
		if keys[pygame.K_s] and player.y + player_vel + 50 < HEIGHT:
			player.y += player_vel


main()