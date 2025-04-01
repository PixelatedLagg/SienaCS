import copy

hints_board = []
for i in range(9):
    hints_board.append(list(map(int, input().split(' '))))
initI, initJ = 0, 0
hints = {}

for i in range(9):
    for j in range(9):
        if hints_board[i][j] == 0:
            continue
        if hints_board[i][j] == 1:
            initI = i
            initJ = j
        hints.update({hints_board[i][j]:(i, j)})

def verifyHint(i, j, num):
    if not num in hints.keys():
        return True
    hint_pos = hints[num]
    if hint_pos[0] == i and hint_pos[1] == j:
        return True
    return False
def verifyBounds(i, j):
    return 0 <= i and i < 9 and 0 <= j and j < 9

directions = [
    (-1, 0), (0, 1), (0, -1), (1, 0)
]

def printBoard(board):
    print()
    for i in range(9):
        row_format = []
        for j in range(9):
            if board[i][j] < 10:
                row_format.append(f"0{board[i][j]} ")
            else:
                row_format.append(f"{board[i][j]} ")
        print(''.join(row_format))

def move(currentI, currentJ, newNum, board):
    if newNum == 82:
        printBoard(board)
        exit()
    for dir in directions:
        if (verifyBounds(currentI + dir[0], currentJ + dir[1]) and verifyHint(currentI + dir[0], currentJ + dir[1], newNum) and (board[currentI + dir[0]][currentJ + dir[1]] == 0 or newNum in hints.keys())):
            newBoard = copy.deepcopy(board)
            newBoard[currentI + dir[0]][currentJ + dir[1]] = newNum
            move(currentI + dir[0], currentJ + dir[1], newNum + 1, newBoard)
    return #dead end!

move(initI, initJ, 2, hints_board)