import pygame
from pygame.locals import *
from character import Player
from level1 import World
from level1 import world_data

#define
FPS = 30
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
tile_size = 50

# init game
pygame.init()
font = pygame.font.SysFont('default', 64)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 
                                 pygame.FULLSCREEN)
fps_clock = pygame.time.Clock()
pygame.display.set_caption('Plant Guy')

#load imiage
bg_img = pygame.image.load('Picture/jungle-background.jpg')

player = Player(100, SCREEN_HEIGHT - 96)
world = World(world_data)

#pagina afsluiten
run = True
while run:
    
    screen.blit(bg_img, (0, 0))

    world.draw()
    player.update()
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.display.update()

pygame.quit()