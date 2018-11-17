from boardFuncs import *
from setUpFuncs import *
from turnFuncs import *
import numpy
import sys
import webbrowser
import random
from Player import *



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

    #CHANGE player 1 and 2 labels
    myfont2 = pygame.font.SysFont("monospace", 40, True)
    label2 = myfont2.render("Player 1", 1, BLACK)
    screen.blit(label2, (860, 100))

    myfont3 = pygame.font.SysFont("monospace", 40, True)
    label3 = myfont3.render("Player 2", 1, BLACK)
    screen.blit(label3, (860, 250))

    #player resource labels
    resource_Font = pygame.font.SysFont("monospace", 25, True)
    player1_resources = resource_Font.render("Lumber: _  Grain: _  Ore: _  Wool: _  Brick: _", 1, BLACK)
    player1_points = resource_Font.render("Victory Points: _  Development Cards: _", 1, BLACK)
    screen.blit(player1_resources, (730, 150))
    screen.blit(player1_points, (750, 180))

    player1_resources = resource_Font.render("Lumber: _  Grain: _  Ore: _  Wool: _  Brick: _", 1, BLACK)
    player1_points = resource_Font.render("Victory Points: _  Development Cards: _", 1, BLACK)
    screen.blit(player1_resources, (730, 300))
    screen.blit(player1_points, (750, 330))

    player1_LumberN = resource_Font.render(str(player1.lumber), 1, (255,255,255))
    player1_GrainN = resource_Font.render(str(player1.grain), 1, (255,255,255))
    player1_OreN = resource_Font.render(str(player1.ore), 1, (255,255,255))
    player1_WoolN = resource_Font.render(str(player1.wool), 1, (255,255,255))
    player1_BrickN = resource_Font.render(str(player1.brick), 1, (255,255,255))
    player1_VPoints = resource_Font.render(str(player1.victoryPoints), 1, (255,255,255))
    player1_devCards = resource_Font.render(str(player1.devCards), 1, (255,255,255))
    screen.blit(player1_LumberN, (811, 150))
    screen.blit(player1_GrainN, (896, 150))
    screen.blit(player1_OreN, (964, 150))
    screen.blit(player1_WoolN, (1044, 150))
    screen.blit(player1_BrickN, (1126, 150))
    screen.blit(player1_VPoints, (893, 180))
    screen.blit(player1_devCards, (1108, 180))

    player2_LumberN = resource_Font.render(str(player2.lumber), 1, (255,255,255))
    player2_GrainN = resource_Font.render(str(player2.grain), 1, (255,255,255))
    player2_OreN = resource_Font.render(str(player2.ore), 1, (255,255,255))
    player2_WoolN = resource_Font.render(str(player2.wool), 1, (255,255,255))
    player2_BrickN = resource_Font.render(str(player2.brick), 1, (255,255,255))
    player2_VPoints = resource_Font.render(str(player2.victoryPoints), 1, (255,255,255))
    player2_devCards = resource_Font.render(str(player2.devCards), 1, (255,255,255))
    screen.blit(player2_LumberN, (811, 300))
    screen.blit(player2_GrainN, (896, 300))
    screen.blit(player2_OreN, (964, 300))
    screen.blit(player2_WoolN, (1044, 300))
    screen.blit(player2_BrickN, (1126, 300))
    screen.blit(player2_VPoints, (893, 330))
    screen.blit(player2_devCards, (1108, 330))
    #

    pygame.display.update()

'''def timeToRoll(screen):
    rolled = False

    while not rolled:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                posx, posy = pygame.mouse.get_pos()

                if 925 <= posx <= 1000 and 650 <= posy <= 680:
                    #getResources(roll_dice(screen))
                    getResources(screen, roll_dice(screen), player1_Lumber, player1_Grain, player1_Ore, player1_Wool, player1_Brick)

                    rolled = True'''


if __name__ == "__main__":
    # define basic attributes
    theBoard = numpy.zeros((ROWS, COLUMNS))
    build_board(theBoard)
    game_over = False
    turn = True
    players = 2
    

    #CHANGE player resources
    player1 = Player()
    player2 = Player()

    # basic pygame modules
    print_board(theBoard)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    

    # start game has been clicked
    #start_game = main_menu(screen)
    screen.fill(BLUE)
    # basic displays
    draw_board(screen, theBoard)
    #setUpSettlement(turn, theBoard, screen)
    draw_items(screen)

    setUpSettlement(turn, theBoard, screen)
    placeRoad(turn, theBoard, screen)

    while not game_over:
        placeRoad(turn, theBoard, screen)
        placeRoad(turn, theBoard, screen)
        placeSettlement(turn, theBoard, screen)
        moveRobber(screen, theBoard)
        placeCity(turn, theBoard, screen)
        #timeToRoll(screen)
        #getResources(roll_dice(screen), player1_Lumber, player1_Grain, player1_Ore, player1_Wool, player1_Brick)
        # rolled = False

        # while not rolled:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             sys.exit()

        #         elif event.type == pygame.MOUSEBUTTONDOWN:
        #             posx, posy = pygame.mouse.get_pos()

        #             if 925 <= posx <= 1000 and 650 <= posy <= 680:
        #                 #getResources(roll_dice(screen))
        #                 getResources(screen, roll_dice(screen), player1, player2)
        #                 print(player1.lumber, player1.grain, player1.ore, player1.wool, player1.brick)
        #                 rolled = True



























