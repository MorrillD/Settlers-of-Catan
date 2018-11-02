from main import *
import pygame
import time
import random


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


def timeToRoll(screen):
    rolled = False

    while not rolled:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                posx, posy = pygame.mouse.get_pos()

                if 925 <= posx <= 1000 and 650 <= posy <= 680:
                    getResources(roll_dice(screen))
                    rolled = True


def getResources(dice):
    pass


def timeToTrade():
    pass


def timeToBuild():
    pass
