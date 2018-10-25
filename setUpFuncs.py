from main import *

def setUpSettlement(turn, board, screen):
    myfont = pygame.font.SysFont("monospace", 20, True)
    if turn:
        text = "Player 1 place a settlement"
    else:
        text = "Player 2 place a settlement"

    label = myfont.render(text, 1, BLACK)
    screen.blit(label, (800, 200))
    pygame.display.update()
    placeSettlement(turn, board, screen)


def setUpRoad(turn, board, screen):
    pass


def placeSettlement(turn, board, screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
