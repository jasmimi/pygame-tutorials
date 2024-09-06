# name: mainmenu.py
# author: Jasmine Amohia
# date: 29/08/24
# desc: menu for player/s to choose which game they want to play

import pygame
import paperscissorsrock
import reaction

pygame.init()

# Window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("Arial", 36)
fontsub = pygame.font.SysFont("Arial", 30)


# Button creation function
def create_button(text, x, y, width, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height), border_radius=10)
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height), border_radius=10)

    txtsurf = fontsub.render(text, True, (255, 255, 255))
    screen.blit(txtsurf, (x + (width / 2 - txtsurf.get_width() / 2), y + (height / 2 - txtsurf.get_height() / 2)))

# Functions to run the games
def start_reaction():
    pygame.quit()
    reaction.main()

def start_paperscissorsrock():
    pygame.quit()
    paperscissorsrock.main()

# Game loop
run = True

while run:
    _image_surf = pygame.image.load("bg.jpg").convert()
    screen.blit(_image_surf, (0,0))

    txt = font.render("RaspberryPi Arcade", True, (255, 255, 255))
    txtoutline = font.render("RaspberryPi Arcade", True, (105, 31, 40))

    screen.blit(txtoutline, (((SCREEN_WIDTH / 2) - txt.get_width() // 2)-2, (SCREEN_HEIGHT / 4)-2))
    screen.blit(txtoutline, (((SCREEN_WIDTH / 2) - txt.get_width() // 2)+2, (SCREEN_HEIGHT / 4)+2))
    screen.blit(txtoutline, (((SCREEN_WIDTH / 2) - txt.get_width() // 2)-2, (SCREEN_HEIGHT / 4)+2))
    screen.blit(txtoutline, (((SCREEN_WIDTH / 2) - txt.get_width() // 2)+2, (SCREEN_HEIGHT / 4)-2))
    screen.blit(txt, ((SCREEN_WIDTH / 2) - txt.get_width() // 2, SCREEN_HEIGHT / 4))


    # Create buttons
    create_button("Paper Scissors Rock", 250, 240, 300, 50, (105, 31, 40), (185, 64, 81), start_paperscissorsrock)
    create_button("Reaction Game", 250, 320, 300, 50, (105, 31, 40), (185, 64, 81), start_reaction)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
