import pygame
from pygame.locals import *
from character import Player_1
from character import Player_2
from character import Button

#define
FPS = 30
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

tile_size = 40
game_over = 0
menu = True

# init game
pygame.init()
font = pygame.font.SysFont('default', 64)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), FULLSCREEN)
fps_clock = pygame.time.Clock()
pygame.display.set_caption('Plant Guy')

#load imiage
bg_img = pygame.image.load('Picture/jungle-background.jpg')
menu_bg_img = pygame.image.load('Picture/bg_menu.jpg')
rest_img = pygame.image.load('Picture/restart.png')
restart_img = pygame.transform.scale(rest_img, (tile_size * 9, tile_size * 3))
ply_img = pygame.image.load('Picture/play.png')
play_img = pygame.transform.scale(ply_img, (tile_size * 9, tile_size * 3))
ext_img = pygame.image.load('Picture/exit.png')
exit_img = pygame.transform.scale(ext_img, (tile_size * 9, tile_size * 3))
mnu_img = pygame.image.load('Picture/menu.png')
menu_img = pygame.transform.scale(mnu_img, (tile_size * 9, tile_size * 3))


spike_group = pygame.sprite.Group()

class World():

  def __init__(self, data):
    self.tile_list = []

    #load images
    MossyStone_img = pygame.image.load('Picture/MossyStone.jpg')
    boom_img = pygame.image.load('Picture/boom.webp')

    row_count = 0
    for row in data:
      col_count = 0
      for tile in row:
        if tile == 1:
          img = pygame.transform.scale(MossyStone_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile)
        elif tile == 2:
          img = pygame.transform.scale(boom_img, (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          tile = (img, img_rect)
          self.tile_list.append(tile)
        elif tile == 3:
          spike = Spike(col_count * tile_size, row_count * tile_size)
          spike_group.add(spike)

        col_count += 1
      row_count += 1

  def draw(self):
    for tile in self.tile_list:
      screen.blit(tile[0], tile[1])
      #pygame.draw.rect(screen, (255,255,255), tile[1], 2)


class Spike(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    img = pygame.image.load('Picture/spike.png')
    self.image = pygame.transform.scale(img, (tile_size, tile_size))  # Scale the image
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
        
  def draw(self):
       spike_group.draw(screen)
       #pygame.draw.rect(screen, (255,255,255), 2)    



world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]   



Player_1 = Player_1(200, SCREEN_HEIGHT - 96)
Player_2 = Player_2(100, SCREEN_HEIGHT - 96)

world = World(world_data)

play_button = Button(SCREEN_WIDTH / 2 - 180, SCREEN_HEIGHT / 4 - 50, play_img)
exit_button = Button(SCREEN_WIDTH / 2 - 180, SCREEN_HEIGHT / 2 + 110, exit_img)
restart_button = Button(SCREEN_WIDTH / 4 - 180, SCREEN_HEIGHT / 2 - 60, restart_img)
menu_button = Button(SCREEN_WIDTH / 2 + 180, SCREEN_HEIGHT / 2 - 60, menu_img)

run = True
while run:
    
    fps_clock.tick(FPS)
    
    screen.blit(menu_bg_img, (0, 0))

    if menu == True:


      if play_button.draw():  
        menu = False  

      if exit_button.draw():  
        run = False  

    
    else:  
      screen.blit(bg_img, (0, 0))

      world.draw()

      spike_group.draw(screen)

      game_over = Player_1.update(game_over)
      game_over = Player_2.update(game_over)

      if game_over == -1:
        if menu_button.draw():
           menu = True
        if restart_button.draw():
            Player_1.reset(200, SCREEN_HEIGHT - 96)
            Player_2.reset(100, SCREEN_HEIGHT - 96)
            game_over = 0
          

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()