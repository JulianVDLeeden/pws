import pygame
from pygame.locals import *
#from character import Player_1, Player_2, Button

#define
FPS = 30
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

tile_size = 40
game_over = 0
menu = True
level = 1

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
game_ovr_img = pygame.image.load('Picture/game_over.jpg')
game_over_img = pygame.transform.scale(game_ovr_img, (SCREEN_WIDTH, SCREEN_HEIGHT))


spike_group = pygame.sprite.Group()
spike_group_2 = pygame.sprite.Group()
finish_group = pygame.sprite.Group()
finish2_group = pygame.sprite.Group()

class World():

  def __init__(self, data):
    self.tile_list = []

    #load images
    MossyStone_img = pygame.image.load('Picture/MossyStone.jpg')
    boom_img = pygame.image.load('Picture/boom.webp')
    spike_img = pygame.image.load('Picture/spike.png')

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
        elif tile == 4:
          finish = Finish(col_count * tile_size, row_count * tile_size)
          finish_group.add(finish)
        elif tile == 5:
          finish2 = Finish2(col_count * tile_size, row_count * tile_size)
          finish2_group.add(finish2)    

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
    self.image = pygame.transform.scale(img, (tile_size, tile_size))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class Finish(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    img = pygame.image.load('Picture/portal.png')
    self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 2)))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class Finish2(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    img = pygame.image.load('Picture/portal2.png')
    self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 2)))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

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
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
          ]       
          
world_data_2 = [
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 5, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
          [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
          [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
          [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
          ] 

world = World(world_data)
world_2 = World(world_data_2)

class Button():
  def __init__(self, x, y, image):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.clicked = False

  def draw(self):
    action = False

    pos = pygame.mouse.get_pos()

    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        action = True
        self.clicked = True
    
    if pygame.mouse.get_pressed()[0] == 0:
      self.clicked = False
    
    screen.blit(self.image, self.rect)

    return action

class Player_1():
  def __init__(self,x,y):
    self.reset(x, y)

  def update(self, game_over):
    dx = 0
    dy = 0
    walk_cooldown = 5

    if game_over == 0:
      #keys inklikken
      key = pygame.key.get_pressed()
      if key[pygame.K_UP] and self.jump == False and self.in_air == False:
        self.vel_y = -15
        self.jump = True
      if key[pygame.K_UP] == False:
        self.jump = False
      if key[pygame.K_LEFT]:
        dx -= 5
        self.counter += 1
        self.direction = -1
      if key[pygame.K_RIGHT]:
        dx += 5
        self.counter += 1
        self.direction = 1
      if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
        self.counter = 0
        self.index = 0
        if self.direction == 1:
          self.image = self.image_right[self.index]
        if self.direction == -1:
          self.image = self.image_left[self.index]

      #animation
      if self.counter > walk_cooldown:
        self.counter = 0
        self.index += 1
        if self.index >= len(self.image_right):
          self.index = 0 
        if self.direction == 1:
          self.image = self.image_right[self.index]
        if self.direction == -1:
          self.image = self.image_left[self.index]

      #zwaartekracht
      self.vel_y += 1
      if self.vel_y > 10:
        self.vel_y = 10
      dy += self.vel_y  
      
      #Kijken of de player ergens tegenaan gaat
      self.in_air = True
      for tile in world.tile_list:
        #x collision
        if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
          dx = 0
        #y collision
        if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
          if self.vel_y < 0:
            dy = tile[1].bottom - self.rect.top
            self.vel_y = 0
          elif self.vel_y >= 0:
            dy = tile[1].top - self.rect.bottom  
            self.vel_y = 0
            self.in_air = False

      #contact met spike
      if pygame.sprite.spritecollide(self, spike_group, False):
        game_over = -1

      #contact met portal
      if pygame.sprite.spritecollide(self, finish_group, False):
        game_over = 1

      #Player verplaatsen
      self.rect.x += dx
      self.rect.y += dy

    screen.blit(self.image, self.rect)
    #pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

    return game_over
  

  def reset(self, x, y):
    self.image_right = []
    self.image_left = []
    self.index = 0
    self.counter = 0
    for number in range (1, 4):
      img_right = pygame.image.load(f'Picture/dwarf{number}.png')
      img_right = pygame.transform.scale(img_right, (tile_size * 1.5, tile_size * 1.5))
      img_left = pygame.transform.flip(img_right, True, False)
      self.image_right.append(img_right)
      self.image_left.append(img_left)
    self.image = self.image_right[self.index]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.vel_y = 0
    self.jump = False
    self.direction = 0
    self.in_air = True

class Player_2():
  def __init__(self,x,y):
    self.reset(x, y)

  def update(self, game_over):
    dx = 0
    dy = 0
    walk_cooldown = 5

    if game_over == 0:
      #keys inklikken
      key = pygame.key.get_pressed()
      if key[pygame.K_w] and self.jump == False:
        self.vel_y = -15
        self.jump = True
      if key[pygame.K_w] == False:
        self.jump = False
      if key[pygame.K_a]:
        dx -= 10
        self.counter += 1
        self.direction = -1
      if key[pygame.K_d]:
        dx += 10
        self.counter += 1
        self.direction = 1
      if key[pygame.K_a] == False and key[pygame.K_d] == False:
        self.counter = 0
        self.index = 0
        if self.direction == 1:
          self.image = self.image_right[self.index]
        if self.direction == -1:
          self.image = self.image_left[self.index]

      #animation
      if self.counter > walk_cooldown:
        self.counter = 0
        self.index += 1
        if self.index >= len(self.image_right):
          self.index = 0 
        if self.direction == 1:
          self.image = self.image_right[self.index]
        if self.direction == -1:
          self.image = self.image_left[self.index]

      #zwaartekracht
      self.vel_y += 1
      if self.vel_y > 10:
        self.vel_y = 10
      dy += self.vel_y  
      
      #Kijken of de player ergens tegenaan gaat
      for tile in world.tile_list:
        #x collision
        if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
          dx = 0
        #y collision
        if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
          if self.vel_y < 0:
            dy = tile[1].bottom - self.rect.top
            self.vel_y = 0
          elif self.vel_y >= 0:
            dy = tile[1].top - self.rect.bottom  
            self.vel_y = 0
            

      #contact met spike
      if pygame.sprite.spritecollide(self, spike_group, False):
        game_over = -1

       #contact met portal
      if pygame.sprite.spritecollide(self, finish2_group, False):
        game_over += 1

      #Player verplaatsen
      self.rect.x += dx
      self.rect.y += dy

    screen.blit(self.image, self.rect)
    #pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

    return game_over
  
  def reset(self, x, y):
    self.image_right = []
    self.image_left = []
    self.index = 0
    self.counter = 0
    for number in range (1, 4):
      img_right = pygame.image.load(f'Picture/elf{number}.png')
      img_right = pygame.transform.scale(img_right, (tile_size, tile_size))
      img_left = pygame.transform.flip(img_right, True, False)
      self.image_right.append(img_right)
      self.image_left.append(img_left)
    self.image = self.image_right[self.index]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.vel_y = 0
    self.jump = False
    self.direction = 0

Player_1 = Player_1(200, SCREEN_HEIGHT - 96)
Player_2 = Player_2(100, SCREEN_HEIGHT - 96)

play_button = Button(SCREEN_WIDTH / 4 - 150, SCREEN_HEIGHT / 2 - 60, play_img)
exit_button = Button(SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT / 2 - 60, exit_img)
restart_button = Button(SCREEN_WIDTH / 2 - 180, SCREEN_HEIGHT / 4 - 80, restart_img)
menu_button = Button(SCREEN_WIDTH / 2 - 180, SCREEN_HEIGHT / 2 + 140, menu_img)

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

      game_over = Player_1.update(game_over)
      game_over = Player_2.update(game_over)

      if game_over == 0:
        world.draw()
        #spike_group.draw(screen)
        #finish_group.draw(screen)
        #finish2_group.draw(screen)
      elif game_over == 1:
        world_2.draw()
        spike_group.draw(screen)
        finish_group.draw(screen)
        finish2_group.draw(screen)

      if game_over == -1:
         screen.blit(game_over_img, (0, 0))

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