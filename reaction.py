# name: reaction.py
# author: Jasmine Amohia
# date: 19/08/24
# desc: single-player game to test players reaction time

import pygame
from random import randrange

pygame.init()

# Window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("Arial", 36)

SCREEN_CHANGE = randrange(1, 15) * 1000

def changeScreenRandom():
    screen.fill((255, 0, 0))
    txtsurf = font.render("Press SPACE", True, (255, 255, 255))
    screen.blit(txtsurf, ((SCREEN_WIDTH / 2) - txtsurf.get_width() // 2, (SCREEN_HEIGHT / 2) - txtsurf.get_height() // 2))

def changeScreenPressedEarly():
    screen.fill((0, 0, 255))
    txtsurf = font.render("You pressed too early!", True, (255, 255, 255))
    screen.blit(txtsurf, ((SCREEN_WIDTH / 2) - txtsurf.get_width() // 2, (SCREEN_HEIGHT / 2) - txtsurf.get_height() // 2))

def changeScreenPressed(time):
    screen.fill((0, 128, 0))
    speed = time / 1000
    text = "You pressed in " + str(round(speed, 3)) + " seconds!"
    txtsurf = font.render(text, True, (255, 255, 255))
    screen.blit(txtsurf, ((SCREEN_WIDTH / 2) - txtsurf.get_width() // 2, (SCREEN_HEIGHT / 2) - txtsurf.get_height() // 2))

# Game loop
run = True
pressed = False
early = True
screen_changed_time = 0
init = True

while run:
    current_time = pygame.time.get_ticks()

    if screen_changed_time == 0 and pressed == False and init:
      screen.fill((0, 0, 0))
      txtsurf = font.render("Get ready to press SPACE", True, (255, 255, 255))
      screen.blit(txtsurf, ((SCREEN_WIDTH / 2) - txtsurf.get_width() // 2, (SCREEN_HEIGHT / 2) - txtsurf.get_height() // 2))
      if current_time >= SCREEN_CHANGE and init:
          changeScreenRandom()
          screen_changed_time = pygame.time.get_ticks()
          early = False

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] == True:
        pressed = True

    if pressed and init:
        if early:
            changeScreenPressedEarly()
            init = False
        else:
            reaction_time = current_time - screen_changed_time
            changeScreenPressed(reaction_time)
            init = False
        pressed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
