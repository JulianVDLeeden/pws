import pygame, sys

from pygame import font
from button import Button

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

SCREEN = pygame.display.set_mode((1280, 720))

bg_img_menu = pygame.image.load('Picture/bg_menu.jpg')

game_status_msg_credits = ''
game_status_msg_niek = ''
game_status_msg_julian = ''

def get_font(size):

def PLAY():
   pygame.display.set_caption('Play')

   while True:

      PLAY_MOUSe_POS = pygame.mouse.get_pos()

      PLAY_BACK = Button(image=none, pos=(640, 460), 
      text_imput='black', font=get_font(75), base_color = 'white', hovering_color = 'green' )
      
      PLAY_BACK.changeColor(PLAY_MOUSe_POS)
      PLAY_BACK.update(SCREEN)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if PLAY_BACK.checkForInput(PLAY_MOUSe_POS):
            main_menu()
        
      pygame.display.update()

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

  while True:
    screen.blit(bg_img_menu(0,0))

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    Menu_TEXT = get_font(100).render('Main Menu', True, '#b68f40')
    MENU_RECT = MENU_TEXT.get_rect(center = (640, 100))

    PLAY_BUTTON = Button(image=pygame.image.load('Picture/MossyStone.jpg'), 
    pos=(640,250), text_imput='PLAY', font=get_font(75), bas_color = '#d7fcd4', hovering_color='white')

    CREDITS= Button(image=pygame.image.load('Picture/MossyStone.jpg'), 
    pos=(640,400), text_imput='CREDITS', font=get_font(75), bas_color = '#d7fcd4', hovering_color='white')

    QUIT_BUTTON = Button(image=pygame.image.load('Picture/MossyStone.jpg'), 
    pos=(640,550), text_imput='QUIT', font=get_font(75), bas_color = '#d7fcd4', hovering_color='white')

    SCREEN.blit(Menu_TEXT, MENU_RECT)
    


main_menu()