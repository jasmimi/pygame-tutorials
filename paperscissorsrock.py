# name: paperscissorsrock.py
# author: Jasmine Amohia
# date: 26/08/24
# desc: two-player game with best of 3 rounds playing paper scissors rock
 
import pygame

pygame.init()

#Window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("Arial", 36)

#Game loop
run = True

while run:
  screen.fill((0, 0, 0))
  txtsurf = font.render("Paper, scissors, rock", True, (255, 255, 255))
  screen.blit(txtsurf, ((SCREEN_WIDTH / 2) - txtsurf.get_width() // 2, (SCREEN_HEIGHT / 2) - txtsurf.get_height() // 2))

  key = pygame.key.get_pressed()
  if key[pygame.K_SPACE] == True:
    print("Meow")

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          run = False

  pygame.display.update()

pygame.quit()