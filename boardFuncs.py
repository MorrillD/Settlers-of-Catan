from globals import *
import pygame


def build_board(board):
    # perimeter starting from 9 o'clock going ccw
    # bottom left side
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
            elif board[r][c] == R_SETTLEMENT:
                print("X", end="    ")
            elif board[r][c] == B_SETTLEMENT:
                print("+", end="    ")
            elif board[r][c] == EMPTY_ROAD:
                print("|", end="    ")
            elif board[r][c] == R_ROAD:
                print("\\", end="    ")
            elif board[r][c] == B_ROAD:
                print("/", end="    ")
            elif board[r][c] == ROBBER:
                print("R", end="    ")
            elif board[r][c] >= 10:
                print(int(board[r][c]), end="   ")
            else:
                print(int(board[r][c]), end="    ")
        print("\n", "")


# draws board and all other items at start of game
def draw_board(screen, board):
    bg = pygame.image.load("BasicBoard.jpg")
    screen.blit(bg, (0, 42))

    for r in range(ROWS):
        for c in range(COLUMNS):
            # draws settlements on screen
            if board[r][c] == R_SETTLEMENT or board[r][c] == R_ROAD:
                pygame.draw.polygon(screen, RED, get_rs_coordinates(r, c))

            elif board[r][c] == B_SETTLEMENT:
                pygame.draw.polygon(screen, DARK_BLUE, get_rs_coordinates(r, c))


    pygame.display.update()


# takes in position of MOUSEBUTTONDOWN and returns corresponding settlement position
# returns 0, 0 if not a correct click
def get_settlement_pos(x, y):
    # top row of settlements
    if 100 <= y <= 120:
        if 245 <= x <= 265:
            return 0, 6
        elif 350 <= x <= 370:
            return 0, 10
        elif 455 <= x <= 475:
            return 0, 14

    # following statements need to be if not elif in case of overlap
    # second row of settlements
    if 125 <= y <= 145:
        if 190 <= x <= 210:
            return 2, 4
        elif 297 <= x <= 317:
            return 2, 8
        elif 402 <= x <= 422:
            return 2, 12
        elif 507 <= x <= 527:
            return 2, 16

    # third row of settlements
    if 190 <= y <= 210:
        if 190 <= x <= 210:
            return 4, 4
        elif 297 <= x <= 317:
            return 4, 8
        elif 402 <= x <= 422:
            return 4, 12
        elif 507 <= x <= 527:
            return 4, 16

    # fourth row of settlements
    if 218 <= y <= 238:
        if 138 <= x <= 158:
            return 6, 2
        elif 245 <= x <= 265:
            return 6, 6
        elif 350 <= x <= 370:
            return 6, 10
        elif 455 <= x <= 475:
            return 6, 14
        elif 560 <= x <= 580:
            return 6, 18

    # fifth row of settlements
    if 280 <= y <= 300:
        if 138 <= x <= 158:
            return 8, 2
        elif 245 <= x <= 265:
            return 8, 6
        elif 350 <= x <= 370:
            return 8, 10
        elif 455 <= x <= 475:
            return 8, 14
        elif 560 <= x <= 580:
            return 8, 18

    # sixth row of settlements
    if 310 <= y <= 330:
        if 85 <= x <= 105:
            return 10, 0
        if 190 <= x <= 210:
            return 10, 4
        elif 297 <= x <= 317:
            return 10, 8
        elif 402 <= x <= 422:
            return 10, 12
        elif 507 <= x <= 527:
            return 10, 16
        elif 612 <= x <= 632:
            return 10, 20

    # seventh row of settlements
    if 372 <= y <= 392:
        if 85 <= x <= 105:
            return 12, 0
        if 190 <= x <= 210:
            return 12, 4
        elif 297 <= x <= 317:
            return 12, 8
        elif 402 <= x <= 422:
            return 12, 12
        elif 507 <= x <= 527:
            return 12, 16
        elif 612 <= x <= 632:
            return 12, 20

    # eighth row of settlements
    if 400 <= y <= 420:
        if 138 <= x <= 158:
            return 14, 2
        elif 245 <= x <= 265:
            return 14, 6
        elif 350 <= x <= 370:
            return 14, 10
        elif 455 <= x <= 475:
            return 14, 14
        elif 560 <= x <= 580:
            return 14, 18

    # ninth row of settlements
    if 465 <= y <= 485:
        if 138 <= x <= 158:
            return 16, 2
        elif 245 <= x <= 265:
            return 16, 6
        elif 350 <= x <= 370:
            return 16, 10
        elif 455 <= x <= 475:
            return 16, 14
        elif 560 <= x <= 580:
            return 16, 18

    # tenth row of settlements
    if 492 <= y <= 512:
        if 190 <= x <= 210:
            return 18, 4
        elif 297 <= x <= 317:
            return 18, 8
        elif 402 <= x <= 422:
            return 18, 12
        elif 507 <= x <= 527:
            return 18, 16

    # eleventh row of settlements
    if 555 <= y <= 575:
        if 190 <= x <= 210:
            return 20, 4
        elif 297 <= x <= 317:
            return 20, 8
        elif 402 <= x <= 422:
            return 20, 12
        elif 507 <= x <= 527:
            return 20, 16

    #
    if 580 <= y <= 600:
        if 245 <= x <= 265:
            return 22, 6
        elif 350 <= x <= 370:
            return 22, 10
        elif 455 <= x <= 475:
            return 22, 16

    else:
        return 0, 0


# takes in position of MOUSEBUTTONDOWN and returns corresponding road position
def get_road_pos(x, y):
    # row 1
    if 108 <= y <= 137:
        if 215 <= x <= 239:
            return 1, 5
        if 261 <= x <= 294:
            return 1, 7
        if 315 <= x <= 354:
            return 1, 9
        if 365 <= x <= 402:
            return 1, 11
        if 422 <= x <= 460:
            return 1, 13
        if 470 <= x <= 507:
            return 1, 15

    # row 3
    if 142 <= y <= 191:
        if 195 <= x <= 205:
            return 3, 4
        if 301 <= x <= 311:
            return 3, 8
        if 407 <= x <= 419:
            return 3, 12
        if 512 <= x <= 522:
            return 3, 16

    # row 5
    if 199 <= y <= 231:
        if 160 <= x <= 190:
            return 5, 3
        if 215 <= x <= 239:
            return 5, 5
        if 261 <= x <= 294:
            return 5, 7
        if 315 <= x <= 354:
            return 5, 9
        if 365 <= x <= 402:
            return 5, 11
        if 422 <= x <= 460:
            return 5, 13
        if 470 <= x <= 507:
            return 5, 15
        if 520 <= x <= 565:
            return 5, 17

    # row 7
    if 234 <= y <= 285:
        if 144 <= x <= 154:
            return 7, 2
        if 248 <= x <= 258:
            return 7, 6
        if 354 <= x <= 364:
            return 7, 10
        if 460 <= x <= 470:
            return 7, 14
        if 564 <= x <= 575:
            return 7, 18

    # row 9
    if 290 <= y <= 322:
        if 107 <= x <= 141:
            return 9, 1
        if 160 <= x <= 190:
            return 9, 3
        if 215 <= x <= 239:
            return 9, 5
        if 261 <= x <= 294:
            return 9, 7
        if 315 <= x <= 354:
            return 9, 9
        if 365 <= x <= 402:
            return 9, 11
        if 422 <= x <= 460:
            return 9, 13
        if 470 <= x <= 507:
            return 9, 15
        if 520 <= x <= 565:
            return 9, 17
        if 574 <= x <= 612:
            return 9, 19

    # row 11
    if 323 <= y <= 378:
        if 91 <= x <= 102:
            return 11, 0
        if 195 <= x <= 205:
            return 11, 4
        if 301 <= x <= 311:
            return 11, 8
        if 407 <= x <= 419:
            return 11, 12
        if 512 <= x <= 522:
            return 11, 16
        if 617 <= x <= 629:
            return 11, 20

    # row 13
    if 380 <= y <= 410:
        if 107 <= x <= 141:
            return 13, 1
        if 160 <= x <= 190:
            return 13, 3
        if 215 <= x <= 239:
            return 13, 5
        if 261 <= x <= 294:
            return 13, 7
        if 315 <= x <= 354:
            return 13, 9
        if 365 <= x <= 402:
            return 13, 11
        if 422 <= x <= 460:
            return 13, 13
        if 470 <= x <= 507:
            return 13, 15
        if 520 <= x <= 565:
            return 13, 17
        if 574 <= x <= 612:
            return 13, 19

    # row 15
    if 415 <= y <= 470:
        if 144 <= x <= 154:
            return 15, 2
        if 248 <= x <= 258:
            return 15, 6
        if 354 <= x <= 364:
            return 15, 10
        if 460 <= x <= 470:
            return 15, 14
        if 564 <= x <= 575:
            return 15, 18

    # row 17
    if 474 <= y <= 505:
        if 160 <= x <= 190:
            return 17, 3
        if 215 <= x <= 239:
            return 17, 5
        if 261 <= x <= 294:
            return 17, 7
        if 315 <= x <= 354:
            return 17, 9
        if 365 <= x <= 402:
            return 17, 11
        if 422 <= x <= 460:
            return 17, 13
        if 470 <= x <= 507:
            return 17, 15
        if 520 <= x <= 565:
            return 17, 17

    # row 19
    if 507 <= y <= 559:
        if 195 <= x <= 205:
            return 19, 4
        if 301 <= x <= 311:
            return 19, 8
        if 407 <= x <= 419:
            return 19, 12
        if 512 <= x <= 522:
            return 19, 16

    # row 21
    if 565 <= y <= 597:
        if 215 <= x <= 239:
            return 21, 5
        if 261 <= x <= 294:
            return 21, 7
        if 315 <= x <= 354:
            return 21, 9
        if 365 <= x <= 402:
            return 21, 11
        if 422 <= x <= 460:
            return 21, 13
        if 470 <= x <= 507:
            return 21, 15

    return 0, 0


# takes the position of road or settlement in the board and returns pointlist to draw on screen
def get_rs_coordinates(r, c):

    # settlement
    if r == 0:
        y1, y2 = 102, 117
        if c == 6:
            x1, x2 = 247, 263
        elif c == 10:
            x1, x2 = 352, 367
        else:
            x1, x2 = 457, 473
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

    # road
    if r == 1:
        if c == 5:
            return [(213, 134), (213, 129), (245, 110), (245, 115)]

    # settlement
    if r == 2:
        y1, y2 = 127, 142
        if c == 4:
            x1, x2 = 192, 207
        elif c == 8:
            x1, x2 = 299, 314
        elif c == 12:
            x1, x2 = 404, 419
        else:
            x1, x2 = 509, 524
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

    # road
    if r == 3:
        pass

    # settlement
    if r == 4:
        y1, y2 = 192, 207
        if c == 4:
            x1, x2 = 192, 207
        elif c == 8:
            x1, x2 = 299, 314
        elif c == 12:
            x1, x2 = 404, 419
        else:
            x1, x2 = 509, 524
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

    # road
    if r == 5:
        pass

    # settlement
    if r == 6:
        y1, y2 = 220, 235
        if c == 2:
            x1, x2 = 140, 155
        elif c == 6:
            x1, x2 = 247, 262
        elif c == 10:
            x1, x2 = 352, 367
        elif c == 14:
            x1, x2 = 457, 472
        else:
            x1, x2 = 562, 577
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

    # road
    if r == 7:
        pass

    # settlement
    if r == 8:
        y1, y2 = 282, 297
        if c == 2:
            x1, x2 = 140, 155
        elif c == 6:
            x1, x2 = 247, 262
        elif c == 10:
            x1, x2 = 352, 367
        elif c == 14:
            x1, x2 = 457, 472
        else:
            x1, x2 = 562, 577
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

    # road
    if r == 9:
        pass

    # settlement
    if r == 10:
        y1, y2 = 312, 327
        if c == 0:
            x1, x2 = 87, 102
        elif c == 4:
            x1, x2 = 192, 207
        elif c == 8:
            x1, x2 = 299, 314
        elif c == 12:
            x1, x2 = 404, 419
        elif c == 16:
            x1, x2 = 509, 524
        else:
            x1, x2 = 614, 629
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

    # road
    if r == 11:
        pass

    # settlement
    if r == 12:
        y1, y2 = 374, 389
        if c == 0:
            x1, x2 = 87, 102
        elif c == 4:
            x1, x2 = 192, 207
        elif c == 8:
            x1, x2 = 299, 314
        elif c == 12:
            x1, x2 = 404, 419
        elif c == 16:
            x1, x2 = 509, 524
        else:
            x1, x2 = 614, 629
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

    # road
    if r == 13:
        pass

    # settlement
    if r == 14:
        y1, y2 = 402, 417
        if c == 2:
            x1, x2 = 140, 155
        elif c == 6:
            x1, x2 = 247, 262
        elif c == 10:
            x1, x2 = 352, 367
        elif c == 14:
            x1, x2 = 457, 472
        else:
            x1, x2 = 562, 577
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

    # road
    if r == 15:
        pass

    # settlement
    if r == 16:
        y1, y2 = 467, 482
        if c == 2:
            x1, x2 = 140, 155
        elif c == 6:
            x1, x2 = 247, 262
        elif c == 10:
            x1, x2 = 352, 367
        elif c == 14:
            x1, x2 = 457, 472
        else:
            x1, x2 = 562, 577
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

    # road
    if r == 17:
        pass

    # settlement
    if r == 18:
        y1, y2 = 492, 507
        if c == 4:
            x1, x2 = 192, 207
        elif c == 8:
            x1, x2 = 299, 314
        elif c == 12:
            x1, x2 = 404, 419
        else:
            x1, x2 = 509, 524
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

    # road
    if r == 19:
        pass

    # settlement
    if r == 20:
        y1, y2 = 557, 572
        if c == 4:
            x1, x2 = 192, 207
        elif c == 8:
            x1, x2 = 299, 314
        elif c == 12:
            x1, x2 = 404, 419
        else:
            x1, x2 = 509, 524
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

    # road
    if r == 21:
        pass

    # settlement
    if r == 22:
        y1, y2 = 582, 597
        if c == 6:
            x1, x2 = 247, 263
        elif c == 10:
            x1, x2 = 352, 367
        else:
            x1, x2 = 457, 473
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
