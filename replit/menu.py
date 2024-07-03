import pygame, sys

from pygame import font
from button import Button

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

SCREEN = pygame.display.set_mode((1280, 720))

bg_img = pygame.image.load('Picture/achtergrond_menu.jpg')

game_status_msg_credits = ''
game_status_msg_niek = ''
game_status_msg_julian = ''

def get_font(size):


def Levels():
  pygame.display.set_caption('Levels')



  

def credits():
  pygame.display.set_caption('Credits')
  game_status_msg_credits = "Gemaakt door: "
  game_status_msg_niek = 'Niek Jerphanion H4b'
  game_status_msg_julian = 'Julian van der Leden H4e'

  game_status_img = font.render(game_status_msg_credits, True, 'white')
  game_status_img = font.render(game_status_msg_niek, True, 'white')
  game_status_img = font.render(game_status_msg_julian, True, 'white')
  
  screen.blit(game_status_msg_credits, (0, 0))
  screen.blit(game_status_msgniek, (0, 0))
  screen.blit(game_status_msg_credits, (0, 0))

def main_menu():
  pygame.display.set_caption('Main_menu')


main_menu()