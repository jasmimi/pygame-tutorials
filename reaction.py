# name: reaction.py
# author: Jasmine Amohia
# date: 23/08/24
# desc: measures players reaction-time to screen colour change

import pygame
from random import randrange

pygame.init()

#Window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("Arial", 36)

SCREEN_CHANGE = randrange(1, 5)

def changeScreenRandom():
  screen.fill((255, 0, 0))
  txtsurf = font.render("SPACE", True, (255, 255, 255))
  screen.blit(txtsurf,((SCREEN_WIDTH/2) - txtsurf.get_width() // 2, (SCREEN_HEIGHT/2) - txtsurf.get_height() // 2))

def changeScreenPressed():
  screen.fill((0, 128, 0))
  txtsurf = font.render("Pressed", True, (255, 255, 255))
  screen.blit(txtsurf,((SCREEN_WIDTH/2) - txtsurf.get_width() // 2, (SCREEN_HEIGHT/2) - txtsurf.get_height() // 2))

#Game loop
run = True
pressed = False
early = True
while run:
  current_time = pygame.time.get_ticks()

  screen.fill((0, 0, 0))
  txtsurf = font.render("Get ready", True, (255, 255, 255))
  screen.blit(txtsurf,((SCREEN_WIDTH/2) - txtsurf.get_width() // 2, (SCREEN_HEIGHT/2) - txtsurf.get_height() // 2))
  
  #pygame.time.wait(SCREEN_CHANGE*1000)
  #changeScreen()

  key = pygame.key.get_pressed()
  if key[pygame.K_SPACE] == True:
    pressed = True
    
    #Before change

    #After change

  if (current_time / 1000) >= SCREEN_CHANGE:
    changeScreenRandom()
    early = False
  if pressed:
    changeScreenPressed()
    if early:
      print('You pressed early!')

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()


pygame.quit()
  