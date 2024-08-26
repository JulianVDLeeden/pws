import pygame
from pygame.locals import *

#define
FPS = 30
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

tile_size = 45
.
# init game
pygame.init()
font = pygame.font.SysFont('default', 64)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                 pygame.FULLSCREEN)
fps_clock = pygame.time.Clock()

class Player_1():
  def __init__(self,x,y):
    img = pygame.image.load('Picture/dwarf.png')
    self.image = pygame.transform.scale(img, (tile_size, tile_size + 10))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.vel_y = 0
    self.jump = False
  def update(self):
    dx = 0
    dy = 0

    #keys inklikken
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and self.jump == False:
      self.vel_y = -15
      self.jump = True
    if key[pygame.K_UP] == False:
      self.jump = False
    if key[pygame.K_LEFT]:
      dx -= 5
    if key[pygame.K_RIGHT]:
      dx += 5

    dy += self.vel_y
    self.vel_y += 1
    if self.vel_y > 10:
      self.vel_y = 10
    #Kijken of de player ergens tegenaan gaat

    #Player verplaatsen
    self.rect.x += dx
    self.rect.y += dy

    if self.rect.bottom > SCREEN_HEIGHT:
      self.rect.bottom = SCREEN_HEIGHT
      dy = 0

    screen.blit(self.image, self.rect)
    pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

class Player_2():
  def __init__(self,x,y):
    img = pygame.image.load('Picture/dwarf2.png')
    self.image = pygame.transform.scale(img, (tile_size, tile_size + 10))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.vel_y = 0
    self.jump = False
  def update(self):
    dx = 0
    dy = 0

    #keys inklikken
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and self.jump == False:
      self.vel_y = -15
      self.jump = True
    if key[pygame.K_w] == False:
      self.jump = False
    if key[pygame.K_a]:
      dx -= 5
    if key[pygame.K_d]:
      dx += 5

    dy += self.vel_y
    self.vel_y += 1
    if self.vel_y > 10:
      self.vel_y = 10
    #Kijken of de player ergens tegenaan gaat

    #Player verplaatsen
    self.rect.x += dx
    self.rect.y += dy

    if self.rect.bottom > SCREEN_HEIGHT:
      self.rect.bottom = SCREEN_HEIGHT
      dy = 0

    screen.blit(self.image, self.rect)
    pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)