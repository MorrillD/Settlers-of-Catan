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

    # draws roads and robber
    for r in range(ROWS):
        for c in range(COLUMNS):
            # roads
            if board[r][c] == R_ROAD:
                pygame.draw.polygon(screen, RED, get_rs_coordinates(r, c))
            elif board[r][c] == B_ROAD:
                pygame.draw.polygon(screen, DARK_BLUE, get_rs_coordinates(r, c))

    # draws settlements and cities
    # seperate loop so that settlements and cities are on top of the road to see outline
    for r in range(ROWS):
        for c in range(COLUMNS):
            if board[r][c] == R_SETTLEMENT:
                pygame.draw.polygon(screen, RED, get_rs_coordinates(r, c))
                pygame.draw.polygon(screen, BLACK, get_rs_coordinates(r, c), 1)
            elif board[r][c] == B_SETTLEMENT:
                pygame.draw.polygon(screen, DARK_BLUE, get_rs_coordinates(r, c))
                pygame.draw.polygon(screen, BLACK, get_rs_coordinates(r, c), 1)
            elif board[r][c] == R_CITY:
                pygame.draw.polygon(screen, RED, get_city_coordinates(r, c))
                pygame.draw.polygon(screen, BLACK, get_city_coordinates(r, c), 1)
            elif board[r][c] == B_CITY:
                pygame.draw.polygon(screen, DARK_BLUE, get_city_coordinates(r, c))
                pygame.draw.polygon(screen, BLACK, get_city_coordinates(r, c), 1)

    # draws robber
    row, col = find_robber(board)
    pygame.draw.circle(screen, BLACK, get_robber_coordinates(row, col), 18)

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
            return [(204, 140), (199, 135), (254, 104), (254, 111)]
        elif c == 7:
            return [(255, 104), (255, 111), (306, 141), (306, 134)]
        elif c == 9:
            return [(306, 141), (306, 134), (359, 104), (359, 111)]
        elif c == 11:
            return [(359, 104), (359, 111), (412, 141), (412, 134)]
        elif c == 13:
            return [(412, 134), (412, 141), (465, 111), (465, 104)]
        elif c == 15:
            return [(465, 111), (465, 104), (519, 136), (515, 141)]

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
        y1, y2 = 140, 198
        if c == 4:
            x1, x2 = 198, 204
        elif c == 8:
            x1, x2 = 304, 310
        elif c == 12:
            x1, x2 = 409, 415
        else:
            x1, x2 = 515, 521
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

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
        if c == 3:
            return[(151, 230), (145, 227), (202, 196), (202, 203)]
        if c == 5:
            return [(202, 196), (202, 203), (254, 233), (254, 226)]
        if c == 7:
            return [(254, 233), (254, 226), (307, 196), (307, 203)]
        if c == 9:
            return [(307, 203), (307, 196), (359, 226), (359, 233)]
        if c == 11:
            return [(359, 233), (359, 226), (412, 196), (412, 203)]
        if c == 13:
            return[(412, 196), (412, 203), (465, 233), (465, 226)]
        if c == 15:
            return [(465, 233), (465, 226), (518, 196), (518, 203)]
        if c == 17:
            return [(518, 203), (518, 196), (573, 229), (567, 232)]

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
        y1, y2 = 231, 290
        if c == 2:
            x1, x2 = 145, 151
        elif c == 6:
            x1, x2 = 251, 257
        elif c == 10:
            x1, x2 = 357, 363
        elif c == 14:
            x1, x2 = 462, 468
        else:
            x1, x2 = 567, 573
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

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
        if c == 1:
            return [(99, 322), (94, 319), (148, 288), (148, 294)]
        elif c == 3:
            return [(148, 288), (148, 294), (201, 325), (201, 319)]
        elif c == 5:
            return [(201, 325), (201, 319), (254, 288), (254, 294)]
        elif c == 7:
            return [(254, 288), (254, 294), (306, 325), (306, 319)]
        elif c == 9:
            return [(306, 325), (306, 319), (359, 288), (359, 294)]
        elif c == 11:
            return [(359, 294), (359, 288), (412, 319), (412, 325)]
        elif c == 13:
            return [(412, 325), (412, 319), (465, 288), (465, 294)]
        elif c == 15:
            return [(465, 294), (465, 288), (517, 319), (517, 325)]
        elif c == 17:
            return [(517, 325), (517, 319), (570, 288), (570, 294)]
        else:
            return [(570, 294), (570, 288), (624, 318), (620, 322)]

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
        y1, y2 = 323, 380
        if c == 0:
            x1, x2 = 93, 99
        elif c == 4:
            x1, x2 = 198, 204
        elif c == 8:
            x1, x2 = 304, 310
        elif c == 12:
            x1, x2 = 409, 415
        elif c == 16:
            x1, x2 = 515, 521
        else:
            x1, x2 = 619, 625
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

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
        if c == 1:
            return[(99, 381), (94, 383), (147, 416), (147, 410)]
        if c == 3:
            return[(147, 410), (147, 416), (202, 386), (202, 380)]
        if c == 5:
            return [(202, 380), (202, 386), (254, 416), (254, 410)]
        if c == 7:
            return [(254, 410), (254, 416), (307, 386), (307, 380)]
        if c == 9:
            return [(307, 380), (307, 386), (359, 416), (359, 410)]
        if c == 11:
            return [(359, 410), (359, 416), (412, 386), (412, 380)]
        if c == 13:
            return[(412, 380), (412, 386), (465, 416), (465, 410)]
        if c == 15:
            return [(465, 410), (465, 416), (518, 386), (518, 380)]
        if c == 17:
            return [(518, 380), (518, 386), (571, 416), (571, 410)]
        if c == 19:
            return [(571, 410), (571, 416), (624, 383), (620, 379)]

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
        y1, y2 = 414, 471
        if c == 2:
            x1, x2 = 145, 151
        elif c == 6:
            x1, x2 = 251, 257
        elif c == 10:
            x1, x2 = 357, 363
        elif c == 14:
            x1, x2 = 462, 468
        else:
            x1, x2 = 567, 573
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

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
        if c == 3:
            return [(151, 472), (146, 475), (201, 506), (201, 500)]
        if c == 5:
            return [(201, 500), (201, 506), (254, 477), (254, 471)]
        if c == 7:
            return [(254, 471), (254, 477), (306, 506), (306, 500)]
        if c == 9:
            return [(306, 500), (306, 506), (359, 477), (359, 471)]
        if c == 11:
            return [(359, 471), (359, 477), (412, 506), (412, 500)]
        if c == 13:
            return [(412, 500), (412, 506), (465, 477), (465, 471)]
        if c == 15:
            return [(465, 471), (465, 477), (517, 506), (517, 500)]
        if c == 17:
            return [(517, 500), (517, 506), (572, 474), (567, 471)]

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
        y1, y2 = 505, 562
        if c == 4:
            x1, x2 = 198, 204
        elif c == 8:
            x1, x2 = 304, 310
        elif c == 12:
            x1, x2 = 409, 415
        else:
            x1, x2 = 515, 521
        return [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

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
        if c == 5:
            return [(204, 563), (199, 566), (254, 597), (254, 591)]
        if c == 7:
            return [(254, 591), (254, 597), (307, 566), (307, 560)]
        if c == 9:
            return [(307, 560), (307, 566), (359, 597), (359, 591)]
        if c == 11:
            return [(359, 591), (359, 597), (412, 566), (412, 560)]
        if c == 13:
            return[(412, 560), (412, 566), (465, 597), (465, 591)]
        if c == 15:
            return [(465, 591), (465, 597), (519, 566), (515, 563)]

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


# returns the coordinates of cities to draw on the screen
def get_city_coordinates(r, c):
    # adds a new tuple of (x, y) to existing settlement tuple
    city = get_rs_coordinates(r, c)
    pos1, pos4 = city[0], city[3]
    x1 = pos1[0]
    x2 = pos4[0]
    x3 = int((x1 + x2) / 2)
    y = pos4[1]
    pos6 = (x3, y)
    y -= 7
    pos4 = (x2, y)
    pos5 = (x3, y)
    city.pop(3)
    city.append(pos4)
    city.append(pos5)
    city.append(pos6)
    return city


def get_robber_pos(x, y):
    if 150 <= y <= 190:
        if 235 <= x <= 270:
            return 3, 6
        if 338 <= x <= 383:
            return 3, 10
        if 443 <= x <= 489:
            return 3, 14

    if 236 <= y <= 283:
        if 175 <= x <= 222:
            return 7, 4
        if 287 <= x <= 334:
            return 7, 8
        if 386 <= x <= 432:
            return 7, 12
        if 495 <= x <= 542:
            return 7, 16

    if 325 <= y <= 371:
        if 122 <= x <= 167:
            return 11, 2
        if 235 <= x <= 270:
            return 11, 6
        if 338 <= x <= 383:
            return 11, 10
        if 443 <= x <= 489:
            return 11, 14
        if 547 <= x <= 596:
            return 11, 18

    if 420 <= y <= 465:
        if 175 <= x <= 222:
            return 15, 4
        if 287 <= x <= 334:
            return 15, 8
        if 386 <= x <= 432:
            return 15, 12
        if 495 <= x <= 542:
            return 15, 16

    if 511 <= y <= 557:
        if 235 <= x <= 270:
            return 19, 6
        if 338 <= x <= 383:
            return 19, 10
        if 443 <= x <= 489:
            return 19, 14

    # invalid click
    return 0, 0


def get_robber_coordinates(r, c):

    if r == 3:
        y = 174
        if c == 6:
            x = 255
        elif c == 10:
            x = 364
        else:
            x = 466

    elif r == 7:
        y = 260
        if c == 4:
            x = 202
        elif c == 8:
            x = 312
        elif c == 12:
            x = 410
        else:
            x = 516

    elif r == 11:
        y = 352
        if c == 2:
            x = 146
        elif c == 6:
            x = 255
        elif c == 10:
            x = 364
        elif c == 14:
            x = 466
        else:
            x = 573

    elif r == 15:
        y = 442
        if c == 4:
            x = 202
        elif c == 8:
            x = 312
        elif c == 12:
            x = 410
        else:
            x = 516

    else:
        y = 534
        if c == 6:
            x = 255
        elif c == 10:
            x = 364
        else:
            x = 466

    coordinate = (x, y)
    return coordinate


# finds the robber on the board
def find_robber(board):
    for c in range(2, 19, 2):
        for r in range(3, 20, 2):
            for i in range(13):
                if board[r][c] - i == ROBBER:
                    return r, c
    # pointless comment