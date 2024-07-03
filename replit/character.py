import pygame
from pygame.locals import *

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class Player():
  def __init__(self,x,y):
    img = pygame.image.load('Picture/dwarf.png')
    self.image = pygame.transform.scale(img, (40, 80))
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
    if key[pygame.K_UP] and not self.jump:
      self.vel_y = -15
      self.jump = True
    if not key[pygame.K_UP]:
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