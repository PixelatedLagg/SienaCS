import copy

row_num, column_num, k_num = map(int, input().split(' '))
initBoard = [[0] * column_num for i in range(row_num)] 

start_coords = []
end_coords = []
for i in range(k_num):
    start_i, start_j, end_i, end_j = map(int, input().split(' '))
    initBoard[start_i][start_j] = k_num + 1
    initBoard[end_i][end_j] = k_num + 1
    start_coords.append([start_i, start_j])
    end_coords.append([end_i, end_j])

directions = [
    (1, 0, 'S'), (-1, 0, 'N'), (0, 1, 'E'), (0, -1, 'W')
]

def inBounds(i, j):
    return -1 < i and i < row_num and -1 < j and j < column_num

def move(posI, posJ, target, board, paths):
    for dir in directions:
        if not inBounds(posI + dir[0], posJ + dir[1]):
            continue
        if board[posI + dir[0]][posJ + dir[1]] == 0:
            newBoard = copy.deepcopy(board)
            newBoard[posI + dir[0]][posJ + dir[1]] = -1
            newPaths = copy.deepcopy(paths)
            newPaths[target - 1].append(dir[2])
            move(posI + dir[0], posJ + dir[1], target, newBoard, newPaths)
        elif posI + dir[0] == end_coords[target - 1][0] and posJ + dir[1] == end_coords[target - 1][1]: #path complete!
            newPaths = copy.deepcopy(paths)
            newPaths[target - 1].append(dir[2])
            if target == k_num:
                for p in newPaths:
                    print(''.join(p))
                exit()
            move(start_coords[target][0], start_coords[target][1], target + 1, board, newPaths)
    return #dead end!

move(start_coords[0][0], start_coords[0][1], 1, initBoard, [[] for i in range(k_num)])
print("NO SOLUTION")