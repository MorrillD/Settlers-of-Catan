from main import *
import pygame


# player places first two settlements
def setUpSettlement(turn, board, screen):
    myfont = pygame.font.SysFont("monospace", 20, True)

    if turn:
        text = "Player 1 place a settlement"
    else:
        text = "Player 2 place a settlement"

    label = myfont.render(text, 1, BLACK)
    screen.blit(label, (800, 200))
    pygame.display.update()

    placed = False
    while not placed:
        for event in pygame.event.get():
            # player quits game
            if event.type == pygame.QUIT:
                sys.exit()

            # player clicks
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

                # get position of click
                posx, posy = event.pos
                row, col = get_settlement_pos(posx, posy)

                # if click is not out of bounds
                if row != 0 or col != 0:
                    # if it is a valid location
                    if isTwoSpaces(board, row, col):
                        # place red piece on player 1's turn
                        if turn:
                            board[row][col] = R_SETTLEMENT
                        # place blue piece on player 2's turn
                        else:
                            board[row][col] = B_SETTLEMENT

                        placed = True

    # erases text prompt
    screen.fill(BLUE)
    draw_board(screen, board)
    pygame.display.update()
    print_board(board)


# determines if a spot chosen by a player is at least two settlement spaces from another settlement or city
def isTwoSpaces(board, row, col):
    # checks if spot selected is empty
    if board[row][col] != EMPTY_SETTLEMENT:
        return False

    # top most spaces
    elif row == 0:
        # checks diagonally below
        if board[2][col - 2] != EMPTY_SETTLEMENT or board[2][col + 2] != EMPTY_SETTLEMENT:
            return False
        else:
            return True

    # bottom most spaces
    elif row == 22:
        # check diagonally above
        if board[20][col - 2] != EMPTY_SETTLEMENT or board[20][col + 2] != EMPTY_SETTLEMENT:
            return False
        else:
            return True

    # using > EMPTY_SETTLEMENT(E_S) instead of == because it may be check a space == 0 not == E_S
    # left most spaces
    elif col == 0:
        # check above and below
        if board[row - 2][0] > EMPTY_SETTLEMENT or board[row + 2][0] > EMPTY_SETTLEMENT:
            return False
        # check diagonally right
        elif board[row - 2][2] > EMPTY_SETTLEMENT or board[row + 2][2] > EMPTY_SETTLEMENT:
            return False
        else:
            return True

    # right most spaces
    elif col == 20:
        # check above and below
        if board[row - 2][20] > EMPTY_SETTLEMENT or board[row + 2][20] > EMPTY_SETTLEMENT:
            return False
        # check diagonally left
        elif board[row - 2][18] > EMPTY_SETTLEMENT or board[row + 2][18] > EMPTY_SETTLEMENT:
            return False
        else:
            return True

    # every other space
    else:
        # check above and below
        if board[row - 2][col] > EMPTY_SETTLEMENT or board[row + 2][col] > EMPTY_SETTLEMENT:
            return False
        # check diagonally left
        elif board[row - 2][col - 2] > EMPTY_SETTLEMENT or board[row + 2][col - 2] > EMPTY_SETTLEMENT:
            return False
        # check diagonally right
        elif board[row - 2][col + 2] > EMPTY_SETTLEMENT or board[row + 2][col + 2] > EMPTY_SETTLEMENT:
            return False
        else:
            return True


def placeRoad(turn, board, screen):
    myfont = pygame.font.SysFont("monospace", 20, True)

    if turn:
        text = "Player 1 place a road"
    else:
        text = "Player 2 place a road"

    label = myfont.render(text, 1, BLACK)
    screen.blit(label, (800, 200))
    pygame.display.update()

    placed = False
    while not placed:
        for event in pygame.event.get():
            # player quits game
            if event.type == pygame.QUIT:
                sys.exit()

            # player clicks
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

                # get position of click
                posx, posy = event.pos
                row, col = get_road_pos(posx, posy)

                if row != 0 or col != 0:
                    # check if connected to settlement
                    if turn:
                        board[row][col] = R_ROAD
                    else:
                        board[row][col] = B_ROAD
                    placed = True

    # erases text prompt
    screen.fill(BLUE)
    draw_board(screen, board)
    pygame.display.update()
    print_board(board)


def placeSettlement(turn, board, screen):
    pass
