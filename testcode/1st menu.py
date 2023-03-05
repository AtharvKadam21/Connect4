import pygame

from G13A_copy import single_player, three_players, two_players

pygame.init()
# Define colors
BLUE = (0,0,255)
WHITE= (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

width = 700
height = 600

# Create the window
screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Connect 4")

# Define font
font = pygame.font.Font(None, 48)

# Create the menu items
menu_items = ["1 Player", "2 Players", "3 Players", "Quit"]

# Create the menu function
def main_menu():
    selected=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected -= 1
                elif event.key == pygame.K_DOWN:
                    selected += 1
                selected%=4
                if event.key == pygame.K_RETURN:
                    if selected == 0:
                        single_player()
                        pass
                    elif selected == 1:
                        two_players()
                        pass
                    elif selected == 2:
                        three_players()
                        pass
                    elif selected == 3:
                        ROW_COUNT = 7
                        COLUMN_COUNT = 9
                        pygame.quit()
                        quit()
        # Draw the menu on the screen
        screen.fill(BLACK)
        for i in range(len(menu_items)):
            if selected == i:
                color = YELLOW
            else:
                color = WHITE
            title = font.render('Connect 4',1,RED)
            label = font.render(menu_items[i], 1, color)
            screen.blit(title, (width/3, height/8))
            screen.blit(label, (width/2, height/(len(menu_items)+1.5)*(i+1.5)))
        pygame.display.update()

# Run the menu
main_menu()

# Clean up and exit
pygame.quit()

