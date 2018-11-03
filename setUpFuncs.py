from main import *
import pygame


# player places first two settlements
# never used after the game is set up
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
                    # check if connected to settlement or road
                    if isNearSR(board, row, col, turn):
                        if turn:
                            board[row][col] = R_ROAD
                        else:
                            board[row][col] = B_ROAD
                        placed = True

    # blit
    screen.fill(BLUE)
    draw_board(screen, board)
    pygame.display.update()
    print_board(board)


# returns true if road trying to be placed is "connected" to settlement, city, or road
def isNearSR(board, r, c, turn):
    if turn:
        # check above for settlement
        if board[r - 1][c] == R_SETTLEMENT or board[r - 1][c] == R_CITY:
            return True

        # check below for settlement
        elif board[r + 1][c] == R_SETTLEMENT or board[r + 1][c] == R_CITY:
            return True

        # check left for settlement and road
        # column 0 will go out of bounds
        if c != 0:
            # check upper left for settlement
            if board[r - 1][c - 1] == R_SETTLEMENT or board[r - 1][c - 1] == R_CITY:
                return True

            # check lower left for settlement
            if board[r + 1][c - 1] == R_SETTLEMENT or board[r + 1][c - 1] == R_CITY:
                return True

            # check up and left for road
            # row 1 will go out of bounds
            if r != 1:
                if board[r + 2][c - 1] == R_ROAD:
                    return True

            # check down and left for road
            # row 21 will go out of bounds
            if r != 21:
                if board[r - 2][c - 1] == R_ROAD:
                    return True

            # check left for road
            # column 1 will go out of bounds
            if c != 1:
                if board[r][c - 2] == R_ROAD:
                    return True

        # check right for roads and settlements
        # column 20 will go out of bounds
        if c != 20:
            # check upper right for settlement
            if board[r - 1][c + 1] == R_SETTLEMENT or board[r - 1][c + 1] == R_CITY:
                return True

            # check lower right for settlement
            if board[r + 1][c + 1] == R_SETTLEMENT or board[r + 1][c + 1] == R_CITY:
                return True

            # check up and right for road
            # row 1 will go out of bounds
            if r != 1:
                if board[r - 2][c + 1] == R_ROAD:
                    return True

            # check down and right for road
            # row 21 will go out of bounds
            if r != 21:
                if board[r + 2][c + 1] == R_ROAD:
                    return True

            # checks right for road
            # column 19 will go out of bounds
            if c != 19:
                if board[r][c + 2] == R_ROAD:
                    return True

    # player 2
    else:
        # check above for settlement
        if board[r - 1][c] == B_SETTLEMENT or board[r - 1][c] == B_CITY:
            return True

        # check below for settlement
        elif board[r + 1][c] == B_SETTLEMENT or board[r + 1][c] == B_CITY:
            return True

        # check left for settlement and road
        # column 0 will go out of bounds
        if c != 0:
            # check upper left for settlement
            if board[r - 1][c - 1] == B_SETTLEMENT or board[r - 1][c - 1] == B_CITY:
                return True

            # check lower left for settlement
            if board[r + 1][c - 1] == B_SETTLEMENT or board[r + 1][c - 1] == B_CITY:
                return True

            # check up and left for road
            # row 1 will go out of bounds
            if r != 1:
                if board[r + 2][c - 1] == B_ROAD:
                    return True

            # check down and left for road
            # row 21 will go out of bounds
            if r != 21:
                if board[r - 2][c - 1] == B_ROAD:
                    return True

            # check left for road
            # column 1 will go out of bounds
            if c != 1:
                if board[r][c - 2] == B_ROAD:
                    return True

        # check right for roads and settlements
        # column 20 will go out of bounds
        if c != 20:
            # check upper right for settlement
            if board[r - 1][c + 1] == B_SETTLEMENT or board[r - 1][c + 1] == B_CITY:
                return True

            # check lower right for settlement
            if board[r + 1][c + 1] == B_SETTLEMENT or board[r + 1][c + 1] == B_CITY:
                return True

            # check up and right for road
            # row 1 will go out of bounds
            if r != 1:
                if board[r - 2][c + 1] == B_ROAD:
                    return True

            # check down and right for road
            # row 21 will go out of bounds
            if r != 21:
                if board[r + 2][c + 1] == B_ROAD:
                    return True

            # checks right for road
            # column 19 will go out of bounds
            if c != 19:
                if board[r][c + 2] == B_ROAD:
                    return True

    # not connected to anything
    return False


def placeSettlement(turn, board, screen):
    pass
