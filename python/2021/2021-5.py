import copy

column_hints = []
column_hints.append(input())
row_hints = []
for i in range(5):
    row_hints.append(input())
column_hints.append(input())
posY, posX = map(int, input().split(' '))
gridNew = [[' ', ' ', ' ', ' ', ' '] for i in range(5)]

def hint(x, y, letter):
    if column_hints[0][x + 1] == letter or column_hints[1][x + 1] == letter: #check columns
        return True
    if row_hints[y][0] == letter or row_hints[y][1] == letter: #check rows
        return True
    if y + x == 4 and (column_hints[0][6] == letter or column_hints[1][0] == letter): #check top right diagonal
        return True
    if y == x and (column_hints[0][0] == letter or column_hints[1][6] == letter): #check bottom right diagonal
        return True
    return False

directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0), 
    (-1, -1), (-1, 1), (1, -1), (1, 1)
]

def in_bounds(x, y):
    return x > -1 and x < 5 and y > -1 and y < 5

def move(currentX, currentY, newLetter, grid):
    if newLetter == 'Z': #DONE!
        for i in range(5):
            print(f"{grid[i][0]}{grid[i][1]}{grid[i][2]}{grid[i][3]}{grid[i][4]}")
        exit()
    for dir in directions:
        if (in_bounds(currentX + dir[0], currentY + dir[1]) and grid[currentY + dir[1]][currentX + dir[0]] == ' ') and hint(currentX + dir[0], currentY + dir[1], newLetter): #right
            newGrid = copy.deepcopy(grid)
            newGrid[currentY + dir[1]][currentX + dir[0]] = newLetter
            move(currentX + dir[0], currentY + dir[1], chr(ord(newLetter) + 1), newGrid)
    return #dead end!

gridNew[posY][posX] = 'A'
move(posX, posY, 'B', gridNew)