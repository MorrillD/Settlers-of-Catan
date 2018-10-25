from globals import *
import pygame


def build_board(board):
    # perimeter starting from 9 o'clock going ccw
    # botom left side
    board[11][0] = EMPTY_ROAD
    board[12][0] = EMPTY_SETTLEMENT
    board[13][1] = EMPTY_ROAD
    board[14][2] = EMPTY_SETTLEMENT
    board[15][2] = EMPTY_ROAD
    board[16][2] = EMPTY_SETTLEMENT
    board[17][3] = EMPTY_ROAD
    board[18][4] = EMPTY_SETTLEMENT
    board[19][4] = EMPTY_ROAD
    board[20][4] = EMPTY_SETTLEMENT
    board[21][5] = EMPTY_ROAD
    board[22][6] = EMPTY_SETTLEMENT
    # bottom side
    board[21][7] = EMPTY_ROAD
    board[20][8] = EMPTY_SETTLEMENT
    board[21][9] = EMPTY_ROAD
    board[22][10] = EMPTY_SETTLEMENT
    board[21][11] = EMPTY_ROAD
    board[20][12] = EMPTY_SETTLEMENT
    board[21][13] = EMPTY_ROAD
    # bottom right side
    board[22][14] = EMPTY_SETTLEMENT
    board[21][15] = EMPTY_ROAD
    board[20][16] = EMPTY_SETTLEMENT
    board[19][16] = EMPTY_ROAD
    board[18][16] = EMPTY_SETTLEMENT
    board[17][17] = EMPTY_ROAD
    board[16][18] = EMPTY_SETTLEMENT
    board[15][18] = EMPTY_ROAD
    board[14][18] = EMPTY_SETTLEMENT
    board[13][19] = EMPTY_ROAD
    board[12][20] = EMPTY_SETTLEMENT
    # top right side
    board[11][20] = EMPTY_ROAD
    board[10][20] = EMPTY_SETTLEMENT
    board[9][19] = EMPTY_ROAD
    board[8][18] = EMPTY_SETTLEMENT
    board[7][18] = EMPTY_ROAD
    board[6][18] = EMPTY_SETTLEMENT
    board[5][17] = EMPTY_ROAD
    board[4][16] = EMPTY_SETTLEMENT
    board[3][16] = EMPTY_ROAD
    board[2][16] = EMPTY_SETTLEMENT
    board[1][15] = EMPTY_ROAD
    board[0][14] = EMPTY_SETTLEMENT
    # top side
    board[1][13] = EMPTY_ROAD
    board[2][12] = EMPTY_SETTLEMENT
    board[1][11] = EMPTY_ROAD
    board[0][10] = EMPTY_SETTLEMENT
    board[1][9] = EMPTY_ROAD
    board[2][8] = EMPTY_SETTLEMENT
    board[1][7] = EMPTY_ROAD
    # top right side
    board[0][6] = EMPTY_SETTLEMENT
    board[1][5] = EMPTY_ROAD
    board[2][4] = EMPTY_SETTLEMENT
    board[3][4] = EMPTY_ROAD
    board[4][4] = EMPTY_SETTLEMENT
    board[5][3] = EMPTY_ROAD
    board[6][2] = EMPTY_SETTLEMENT
    board[7][2] = EMPTY_ROAD
    board[8][2] = EMPTY_SETTLEMENT
    board[9][1] = EMPTY_ROAD
    board[10][0] = EMPTY_SETTLEMENT
    # the rest of the roads and settlement spaces
    for c in range(8, 13, 4):
        board[2][c] = EMPTY_SETTLEMENT
        board[3][c] = EMPTY_ROAD
        board[4][c] = EMPTY_SETTLEMENT

    for c in range(6, 15, 4):
        board[6][c] = EMPTY_SETTLEMENT
        board[7][c] = EMPTY_ROAD
        board[8][c] = EMPTY_SETTLEMENT

    for c in range(4, 17, 4):
        board[10][c] = EMPTY_SETTLEMENT
        board[11][c] = EMPTY_ROAD
        board[12][c] = EMPTY_SETTLEMENT

    for c in range(8, 13, 4):
        board[-3][c] = EMPTY_SETTLEMENT
        board[-4][c] = EMPTY_ROAD
        board[-5][c] = EMPTY_SETTLEMENT

    for c in range(6, 15, 4):
        board[-7][c] = EMPTY_SETTLEMENT
        board[-8][c] = EMPTY_ROAD
        board[-9][c] = EMPTY_SETTLEMENT

    for c in range(5, 16, 2):
        board[5][c] = EMPTY_ROAD

    for c in range(3, 18, 2):
        board[9][c] = EMPTY_ROAD

    for c in range(3, 18, 2):
        board[13][c] = EMPTY_ROAD

    for c in range(5, 16, 2):
        board[17][c] = EMPTY_ROAD

    # numbering
    board[7][4] = 2
    board[3][10] = 3
    board[15][8] = 3
    board[7][12] = 4
    board[19][10] = 4
    board[11][14] = 5
    board[11][2] = 5
    board[3][6] = 6
    board[15][12] = 6
    board[15][4] = ROBBER
    board[3][14] = 8
    board[19][6] = 8
    board[7][8] = 9
    board[11][18] = 9
    board[11][6] = 10
    board[7][16] = 10
    board[11][10] = 11
    board[19][14] = 11
    board[15][16] = 12


def print_board(board):
    for r in range(ROWS):
        for c in range(COLUMNS):
            if board[r][c] == 0:
                print(" ", end="    ")
            elif board[r][c] == EMPTY_SETTLEMENT:
                print("O", end="    ")
            elif board[r][c] == EMPTY_ROAD:
                print("|", end="    ")
            elif board[r][c] == ROBBER:
                print("R", end="    ")
            elif board[r][c] >= 10:
                print(int(board[r][c]), end="   ")
            else:
                print(int(board[r][c]), end="    ")
        print("\n", "")


# draws board and all other items at start of game
def draw_board(screen):
    screen.fill(BLUE)
    bg = pygame.image.load("BasicBoard.jpg")
    screen.blit(bg, (0, 42))
    pygame.display.update()



