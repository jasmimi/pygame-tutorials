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

def instructions():
  start_time = pygame.time.get_ticks()
  while pygame.time.get_ticks() - start_time < 10000:
    screen.fill((138, 206, 0))
    txth1 = font.render("Best of 3 rounds", True, (0, 0, 0))
    txth2 = font.render("Choose your action by the last seond", True, (0, 0, 0))
    txth3 = font.render("P1: paper=a, scissors=s, rock=d", True, (0, 0, 0))
    txth4 = font.render("P2: paper=LEFT, scissors=DOWN, rock=RIGHT", True, (0, 0, 0))
    screen.blit(txth1, ((SCREEN_WIDTH / 2) - txth1.get_width() // 2, ((SCREEN_HEIGHT / 2) - txth1.get_height()) - 40 ))
    screen.blit(txth2, ((SCREEN_WIDTH / 2) - txth2.get_width() // 2, ((SCREEN_HEIGHT / 2) - txth2.get_height() // 6) - 40))
    screen.blit(txth3, ((SCREEN_WIDTH / 2) - txth3.get_width() // 2, ((SCREEN_HEIGHT / 2) - txth3.get_height()) + 40 ))
    screen.blit(txth4, ((SCREEN_WIDTH / 2) - txth4.get_width() // 2, ((SCREEN_HEIGHT / 2) - txth4.get_height() // 6) + 40))
    pygame.display.update()
  return False

def rounds():
  for __ in range(3):
    if __ == 0:
      r1 = True
      r2, r3 = False, False
    if __ == 1:
      r2 = True
      r1, r3 = False, False
    elif __ == 2:
      r3 = True
      r1, r2 = False, False

    for _ in range(3, 0, -1):
      screen.fill((138, 206, 0))
      txth1 = font.render(str(_), True, (0, 0, 0))
      screen.blit(txth1, ((SCREEN_WIDTH / 2) - txth1.get_width() // 2, (SCREEN_HEIGHT / 2) - txth1.get_height() // 2 ))
      pygame.display.update()
      pygame.time.delay(1000)
    
    screen.fill((138, 206, 0))
    round = "Round " + str(__+1)
    txth1 = font.render(round, True, (0, 0, 0))
    txth2 = font.render("P1 chose X, P2 chose Y. Result: Z", True, (0, 0, 0))
    screen.blit(txth1, ((SCREEN_WIDTH / 2) - txth1.get_width() // 2, (SCREEN_HEIGHT / 2) - txth1.get_height() ))
    screen.blit(txth2, ((SCREEN_WIDTH / 2) - txth2.get_width() // 2, (SCREEN_HEIGHT / 2) - txth2.get_height() // 6))
    pygame.display.update()
    pygame.time.delay(5000)
  
  screen.fill((138, 206, 0))
  txth1 = font.render("Game over!", True, (0, 0, 0))
  txth2 = font.render("Result: X", True, (0, 0, 0))
  screen.blit(txth1, ((SCREEN_WIDTH / 2) - txth1.get_width() // 2, (SCREEN_HEIGHT / 2) - txth1.get_height() ))
  screen.blit(txth2, ((SCREEN_WIDTH / 2) - txth2.get_width() // 2, (SCREEN_HEIGHT / 2) - txth2.get_height() // 6))
  pygame.display.update()

#Game loop
run = True
init = True
screen_time = 0
p1_score = 0
p2_score = 0

while run:
  if init:
    screen.fill((138, 206, 0))
    txth1 = font.render("Paper, scissors, rock", True, (0, 0, 0))
    txth2 = font.render("Press SPACE to start", True, (0, 0, 0))
    screen.blit(txth1, ((SCREEN_WIDTH / 2) - txth1.get_width() // 2, (SCREEN_HEIGHT / 2) - txth1.get_height() ))
    screen.blit(txth2, ((SCREEN_WIDTH / 2) - txth2.get_width() // 2, (SCREEN_HEIGHT / 2) - txth2.get_height() // 6))
    pygame.display.update()

  key = pygame.key.get_pressed()
  if key[pygame.K_SPACE] and init:
    init = instructions()
    rounds()

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          run = False

  pygame.display.update()

pygame.quit()