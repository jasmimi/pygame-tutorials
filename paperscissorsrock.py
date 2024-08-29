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
    txth2 = font.render("Choose your action", True, (0, 0, 0))
    txth3 = font.render("P1: paper=a, scissors=s, rock=d", True, (0, 0, 0))
    txth4 = font.render("P2: paper=LEFT, scissors=DOWN, rock=RIGHT", True, (0, 0, 0))
    screen.blit(txth1, ((SCREEN_WIDTH / 2) - txth1.get_width() // 2, ((SCREEN_HEIGHT / 2) - txth1.get_height()) - 40 ))
    screen.blit(txth2, ((SCREEN_WIDTH / 2) - txth2.get_width() // 2, ((SCREEN_HEIGHT / 2) - txth2.get_height() // 6) - 40))
    screen.blit(txth3, ((SCREEN_WIDTH / 2) - txth3.get_width() // 2, ((SCREEN_HEIGHT / 2) - txth3.get_height()) + 40 ))
    screen.blit(txth4, ((SCREEN_WIDTH / 2) - txth4.get_width() // 2, ((SCREEN_HEIGHT / 2) - txth4.get_height() // 6) + 40))
    pygame.display.update()
  return False

def rounds():
    p1_scores, p2_scores = 0, 0
    for round_num in range(3):
        screen.fill((138, 206, 0))
        txth1 = font.render(f"Round {round_num + 1}", True, (0, 0, 0))
        screen.blit(txth1, ((SCREEN_WIDTH / 2) - txth1.get_width() // 2, SCREEN_HEIGHT / 4))
        pygame.display.update()
        pygame.time.delay(2000)

        # Countdown before choice
        for _ in range(3, 0, -1):
            screen.fill((138, 206, 0))
            txth1 = font.render(str(_), True, (0, 0, 0))
            screen.blit(txth1, ((SCREEN_WIDTH / 2) - txth1.get_width() // 2, (SCREEN_HEIGHT / 2) - txth1.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(1000)

        p1_score, p2_score, p1_choice, p2_choice, result = round()
        p1_scores += p1_score
        p2_scores += p2_score

        screen.fill((138, 206, 0))
        result_text = f"P1 chose {p1_choice}, P2 chose {p2_choice}. Result: {result}"
        txth1 = font.render(result_text, True, (0, 0, 0))
        screen.blit(txth1, ((SCREEN_WIDTH / 2) - txth1.get_width() // 2, SCREEN_HEIGHT / 2))
        pygame.display.update()
        pygame.time.delay(3000)
    
    screen.fill((138, 206, 0))
    if p1_scores > p2_scores:
        winner_text = "P1 wins the game!"
    elif p2_scores > p1_scores:
        winner_text = "P2 wins the game!"
    else:
        winner_text = "It's a tie!"
    
    txth1 = font.render("Game over!", True, (0, 0, 0))
    txth2 = font.render(winner_text, True, (0, 0, 0))
    screen.blit(txth1, ((SCREEN_WIDTH / 2) - txth1.get_width() // 2, SCREEN_HEIGHT / 3))
    screen.blit(txth2, ((SCREEN_WIDTH / 2) - txth2.get_width() // 2, SCREEN_HEIGHT / 2))
    pygame.display.update()
    pygame.time.delay(5000)

def round():
    p1_choice = p2_choice = None
    while not (p1_choice and p2_choice):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    p1_choice = 'paper'
                elif event.key == pygame.K_s:
                    p1_choice = 'scissors'
                elif event.key == pygame.K_d:
                    p1_choice = 'rock'
                elif event.key == pygame.K_LEFT:
                    p2_choice = 'paper'
                elif event.key == pygame.K_DOWN:
                    p2_choice = 'scissors'
                elif event.key == pygame.K_RIGHT:
                    p2_choice = 'rock'

    if p1_choice == p2_choice:
        return 0, 0, p1_choice, p2_choice, "Tie"
    elif (p1_choice == 'rock' and p2_choice == 'scissors') or \
         (p1_choice == 'scissors' and p2_choice == 'paper') or \
         (p1_choice == 'paper' and p2_choice == 'rock'):
        return 1, 0, p1_choice, p2_choice, "P1 wins"
    else:
        return 0, 1, p1_choice, p2_choice, "P2 wins"

#Game loop
run = True
init = True

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