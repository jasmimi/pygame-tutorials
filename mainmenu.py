# wip doesnt work
import pygame#
#import paperscissorsrock
import reaction

pygame.init()

# Window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("Arial", 36)

# Game loop
run = True

while run:

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] == True:
        reaction.main()


    pygame.display.update()

pygame.quit()
