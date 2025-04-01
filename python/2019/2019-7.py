import itertools
import copy

k = int(input())
initBoard = []
for i in range(k):
    initBoard.append(list(input()))
oPos = []
for i in range(k):
    for j in range(k):
        if initBoard[i][j] == 'O':
            oPos.append([i, j])

def pairOfC(c1, c2):
    return c1 == c2 and c1 != 'O'

def inRange(a, b):
    return -1 < a and a < k and -1 < b and b < k

def checkRowCol(i, j, c, board):
    col = []
    row = board[i]
    count_col = 0
    count_row = 0
    for _i in range(k):
        col.append(board[_i][j])
        if board[_i][j] == c:
            count_col += 1
    for _i in row:
        if _i == c:
            count_row += 1
    if count_row == k / 2 or count_col == k / 2:
        return False
    col[i] = c
    if max(len(list(v)) for g, v in itertools.groupby(col) if g == c) > 2:
        return False
    row[j] = c
    if max(len(list(v)) for g, v in itertools.groupby(row) if g == c) > 2:
        return False
    return True

def move(i, j, o_i, board):
    if checkRowCol(i, j, 'W', board):
        newBoard = copy.deepcopy(board)
        newBoard[i][j] = 'W'
        if o_i == len(oPos) - 1: #solution!
            for _i in newBoard:
                print(''.join(_i))
            exit()
        move(oPos[o_i + 1][0], oPos[o_i + 1][1], o_i + 1, newBoard)
    if checkRowCol(i, j, 'B', board):
        newBoard = copy.deepcopy(board)
        newBoard[i][j] = 'B'
        if o_i == len(oPos) - 1: #solution!
            for _i in newBoard:
                print(''.join(_i))
            exit()
        move(oPos[o_i + 1][0], oPos[o_i + 1][1], o_i + 1, newBoard)
    return #dead end!

move(oPos[0][0], oPos[0][1], 0, initBoard)