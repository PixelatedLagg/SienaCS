import copy

possible_moves = [
    [1, 3, 5],
    [3, 4, 6],
    [1, 4, 7],
    [6],
    [6], 
    [3, 6, 8],
    [3, 4, 8, 9],
    [4, 6, 9],
    [6],
    [6],
    [5, 8, 11],
    [8, 6, 9],
    [11, 9, 7]
]
#0 empty, 1 frog, 2 red frog
num_frogs = int(input())
initBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(num_frogs - 1):
    initBoard[int(input())] = 1
initBoard[int(input())] = 2

def frog_move(board, moves):
    if len(moves) == num_frogs - 1: #done!
        for m in moves:
            print(f"{m[0]}-{m[1]}")
        exit()
    for i in range(13):
        if board[i] != 0:
            for move in possible_moves[i]:
                if board[(-1 * i) + (2 * move)] == 0 and board[move] == 1:
                    newBoard = copy.deepcopy(board)
                    newBoard[(-1 * i) + (2 * move)] = board[i]
                    newBoard[move] = 0
                    newBoard[i] = 0
                    newMoves = copy.deepcopy(moves)
                    newMoves.append((i, (-1 * i) + (2 * move)))
                    frog_move(newBoard, newMoves)
    return #dead end!

frog_move(initBoard, [])
print("No Solution Found")