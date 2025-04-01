hasBeenToBlock = [[False] * 10 for _ in range(10)]
blockTolls = [[] for _ in range(10)]

for i in range(10):
    blockTolls[i] = list(map(int, input().split(' ')))

moves = []
leastsum = float("inf")
sum = 0

def randomMove(x, y, sum):
    global leastsum
    global moves
    global hasBeenToBlock

    if x == 9 and y == 9: #reached end!
        leastsum = min(leastsum, sum)
        return
    else:
        if sum > leastsum: #sum already bigger than leastsum, cancel!
            return
        sum += blockTolls[x][y]
        hasBeenToBlock[x][y] = True
        moves.append((x, y))

        if x > 0 and hasBeenToBlock[x - 1][y] == False:
            randomMove(x - 1, y, sum)
        if y > 0 and hasBeenToBlock[x][y - 1] == False:
            randomMove(x, y - 1, sum)
        if 9 > x and hasBeenToBlock[x + 1][y] == False:
            randomMove(x + 1, y, sum)
        if 9 > y and hasBeenToBlock[x][y + 1] == False:
            randomMove(x, y + 1, sum)
    
    #dead end, backtracking time :)
    moves.pop()
    hasBeenToBlock[x][y] = False
    sum -= blockTolls[x][y]

randomMove(0, 0, sum)
print(leastsum)