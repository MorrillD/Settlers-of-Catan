from main import *
import pygame
import time
import random
import sys
import Player

random.seed()


def roll_dice(screen):
    # displays blank dice while rolling
    dv = pygame.image.load("blankdice.jpg")
    screen.blit(dv, (900, 590))
    screen.blit(dv, (975, 590))
    pygame.display.update()

    time.sleep(.5)

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(die1)
    print(die2)

    # die value for die 1
    if die1 == 1:
        dv = pygame.image.load("dice1.jpg")
    elif die1 == 2:
        dv = pygame.image.load("dice2.jpg")
    elif die1 == 3:
        dv = pygame.image.load("dice3.jpg")
    elif die1 == 4:
        dv = pygame.image.load("dice4.jpg")
    elif die1 == 5:
        dv = pygame.image.load("dice5.jpg")
    elif die1 == 6:
        dv = pygame.image.load("dice6.jpg")

    screen.blit(dv, (900, 590))

    # die value for die 2
    if die2 == 1:
        dv = pygame.image.load("dice1.jpg")
    elif die2 == 2:
        dv = pygame.image.load("dice2.jpg")
    elif die2 == 3:
        dv = pygame.image.load("dice3.jpg")
    elif die2 == 4:
        dv = pygame.image.load("dice4.jpg")
    elif die2 == 5:
        dv = pygame.image.load("dice5.jpg")
    elif die2 == 6:
        dv = pygame.image.load("dice6.jpg")

    screen.blit(dv, (975, 590))
    pygame.display.update()
    return die1 + die2


'''def timeToRoll(screen, turn):
    dice = pygame.image.load("dice1.jpg")
    screen.blit(dice, (900, 590))
    screen.blit(dice, (975, 590))

    # draw button
    pygame.draw.rect(screen, GRAY, (925, 650, 75, 30))
    pygame.draw.rect(screen, BLACK, (925, 650, 75, 30), 2)

    myfont = pygame.font.SysFont("monospace", 20, True)
    label = myfont.render("Roll!", 1, BLACK)
    screen.blit(label, (935, 655))

    myfont = pygame.font.SysFont("monospace", 20, True)
    if turn:
        text = "Player 1, roll the dice"
    else:
        text = "Player 2, roll the dice"

    label = myfont.render(text, 1, BLACK)
    screen.blit(label, (800, 200))

    pygame.display.update()

    rolled = False

    while not rolled:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                posx, posy = pygame.mouse.get_pos()

                if 925 <= posx <= 1000 and 650 <= posy <= 680:
                    getResources(roll_dice(screen))
                    rolled = True'''


def getResources(screen, dice, player1, player2):
    player1.resources(dice)
    player2.resources(dice)

    
    resource_Font = pygame.font.SysFont("monospace", 25, True)
    pygame.draw.rect(screen, BLUE, (811, 150, 20, 20))
    pygame.draw.rect(screen, BLUE, (896, 150, 20, 20))
    pygame.draw.rect(screen, BLUE, (964, 150, 20, 20))
    pygame.draw.rect(screen, BLUE, (1044, 150, 20, 20))
    pygame.draw.rect(screen, BLUE, (1126, 150, 20, 20))
    player1_LumberN = resource_Font.render(str(player1.lumber), 1, (255,255,255))
    player1_GrainN = resource_Font.render(str(player1.grain), 1, (255,255,255))
    player1_OreN = resource_Font.render(str(player1.ore), 1, (255,255,255))
    player1_WoolN = resource_Font.render(str(player1.wool), 1, (255,255,255))
    player1_BrickN = resource_Font.render(str(player1.brick), 1, (255,255,255))
    screen.blit(player1_LumberN, (811, 150))
    screen.blit(player1_GrainN, (896, 150))
    screen.blit(player1_OreN, (964, 150))
    screen.blit(player1_WoolN, (1044, 150))
    screen.blit(player1_BrickN, (1126, 150))

    pygame.draw.rect(screen, BLUE, (811, 300, 20, 20))
    pygame.draw.rect(screen, BLUE, (896, 300, 20, 20))
    pygame.draw.rect(screen, BLUE, (964, 300, 20, 20))
    pygame.draw.rect(screen, BLUE, (1044, 300, 20, 20))
    pygame.draw.rect(screen, BLUE, (1126, 300, 20, 20))
    player1_LumberN = resource_Font.render(str(player2.lumber), 1, (255,255,255))
    player1_GrainN = resource_Font.render(str(player2.grain), 1, (255,255,255))
    player1_OreN = resource_Font.render(str(player2.ore), 1, (255,255,255))
    player1_WoolN = resource_Font.render(str(player2.wool), 1, (255,255,255))
    player1_BrickN = resource_Font.render(str(player2.brick), 1, (255,255,255))
    screen.blit(player1_LumberN, (811, 300))
    screen.blit(player1_GrainN, (896, 300))
    screen.blit(player1_OreN, (964, 300))
    screen.blit(player1_WoolN, (1044, 300))
    screen.blit(player1_BrickN, (1126, 300))

    pygame.display.flip()


def timeToTrade():
    pass


def timeToBuild():
    pass


def moveRobber(screen, board):
    # loops until player makes a valid move
    r1, c1 = find_robber(board)
    placed = False
    while not placed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                posx, posy = pygame.mouse.get_pos()
                r2, c2 = get_robber_pos(posx, posy)

                # if valid placement
                if r2 != 0 and c2 != 0:
                    if r1 != r2 or c1 != c2:
                        placed = True

    board[r1][c1] -= ROBBER
    board[r2][c2] += ROBBER
    print_board(board)
    draw_board(screen, board)
