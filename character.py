import pygame
from pygame.locals import *

#define
FPS = 30
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

tile_size = 40

# init game
pygame.init()
font = pygame.font.SysFont('default', 64)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
fps_clock = pygame.time.Clock()

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
        col_count += 1
      row_count += 1

  def draw(self):
    for tile in self.tile_list:
      screen.blit(tile[0], tile[1])
      pygame.draw.rect(screen, (255,255,255), tile[1], 2)

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
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world = World(world_data)

class Player_1():
  def __init__(self,x,y):
    self.image_right = []
    self.image_left = []
    self.index = 0
    self.counter = 0
    for number in range (1, 4):
      img_right = pygame.image.load(f'Picture/dwarf{number}.png')
      img_right = pygame.transform.scale(img_right, (tile_size * 2, tile_size * 2))
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

  def update(self):
    dx = 0
    dy = 0
    walk_cooldown = 5

    #keys inklikken
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and self.jump == False:
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

    #Player verplaatsen
    self.rect.x += dx
    self.rect.y += dy

    if self.rect.bottom > SCREEN_HEIGHT:
      self.rect.bottom = SCREEN_HEIGHT
      dy = 0

    screen.blit(self.image, self.rect)
    pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)


class Player_2():
  def __init__(self,x,y):
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

  def update(self):
    dx = 0
    dy = 0
    walk_cooldown = 5

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

    #Player verplaatsen
    self.rect.x += dx
    self.rect.y += dy

    if self.rect.bottom > SCREEN_HEIGHT:
      self.rect.bottom = SCREEN_HEIGHT
      dy = 0

    screen.blit(self.image, self.rect)
    pygame.draw.rect(screen, (0, 0, 0), self.rect, 2) 
 