currentLetter = chr(ord('a') - 1)
posX = 0
posY = 0
board = [[' '] * 18 for i in range(18)]
board[0][0] = '#'
super_break = False
dir = 'E'

while True:
    input_ = input()
    if input_ == 'Q' or super_break == True:
        break
    if (input_ == 'F'):
        k = int(input())
        while k != 0:
            modX = 0
            modY = 0
            if dir == 'N':
                modY = -1
            elif dir == 'E':
                modX = 1
            elif dir == 'S':
                modY = 1
            elif dir == 'W':
                modX = -1
            newX = posX + modX
            newY = posY + modY
            if newX < 0 or newX > 17 or newY < 0 or newY > 17:
                super_break = True
                break
            posX = newX
            posY = newY
            if currentLetter == 'z':
                currentLetter = 'A'
            else:
                currentLetter = chr(ord(currentLetter) + 1)
            board[posY][posX] = currentLetter
            k -= 1
    if (input_ == 'R'):
        if dir == 'N':
            dir = 'E'
        elif dir == 'E':
            dir = 'S'
        elif dir == 'S':
            dir = 'W'
        elif dir == 'W':
            dir = 'N'
    if (input_ == 'L'):
        if dir == 'N':
            dir = 'W'
        elif dir == 'W':
            dir = 'S'
        elif dir == 'S':
            dir = 'E'
        elif dir == 'E':
            dir = 'N'
    if (input_ == 'B'):
        k = int(input())
        while k != 0:
            modX = 0
            modY = 0
            if dir == 'N':
                modY = 1
            elif dir == 'E':
                modX = -1
            elif dir == 'S':
                modY = -1
            elif dir == 'W':
                modX = 1
            newX = posX + modX
            newY = posY + modY
            if newX < 0 or newX > 17 or newY < 0 or newY > 17:
                super_break = True
                break
            posX = newX
            posY = newY
            if currentLetter == 'z':
                currentLetter = 'A'
            else:
                currentLetter = chr(ord(currentLetter) + 1)
            board[posY][posX] = currentLetter
            k -= 1

print("********************")
for i in range(18):
    print(f"*{''.join(board[i])}*")
print("********************")