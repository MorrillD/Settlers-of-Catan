from boardFuncs import *
from setUpFuncs import *
from turnFuncs import *
import numpy
import sys
import webbrowser
import random



random.seed(1)


def main_menu(screen):
    # background
    screen.fill(TAN)
    bg = pygame.image.load("Settlers.jpg")
    screen.blit(bg, (0, 0))

    # text
    myfont = pygame.font.SysFont("monospace", 30, True)

    # start game button
    pygame.draw.rect(screen, GRAY, (917, 450, 250, 40))
    pygame.draw.rect(screen, BLACK, (917, 450, 250, 40), 2)
    label = myfont.render("Start Game!", 1, BLACK)
    screen.blit(label, (948, 455))

    # rules button
    pygame.draw.rect(screen, GRAY, (917, 350, 250, 40))
    pygame.draw.rect(screen, BLACK, (917, 350, 250, 40), 2)
    label = myfont.render("Read Rules!", 1, BLACK)
    screen.blit(label, (948, 355))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                posx, posy = pygame.mouse.get_pos()

                # start game
                if 917 <= posx <= 917+250 and 450 <= posy <= 450+40:
                    return True
                # rules button
                elif 917 <= posx <= 917+250 and 350 <= posy <= 350+40:
                    webbrowser.open("http://www.ultracatan.com/game-rules.php")


def draw_items(screen):
    dice = pygame.image.load("dice1.jpg")
    screen.blit(dice, (900, 590))
    screen.blit(dice, (975, 590))

    # draw button
    pygame.draw.rect(screen, GRAY, (925, 650, 75, 30))
    pygame.draw.rect(screen, BLACK, (925, 650, 75, 30), 2)

    myfont = pygame.font.SysFont("monospace", 20, True)
    label = myfont.render("Roll!", 1, BLACK)
    screen.blit(label, (935, 655))

    pygame.display.update()


if __name__ == "__main__":
    # define basic attributes
    theBoard = numpy.zeros((ROWS, COLUMNS))
    build_board(theBoard)
    game_over = False
    turn = True
    players = 2

    # basic pygame modules
    print_board(theBoard)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # start game has been clicked
    # start_game = main_menu(screen)

    # basic displays
    draw_board(screen)
    #setUpSettlement(turn, theBoard, screen)
    draw_items(screen)

    while not game_over:
        timeToRoll(screen)
