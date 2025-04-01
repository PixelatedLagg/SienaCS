rows, columns = map(int, input().split(' '))
board = [0] * rows
for i in range(rows):
    board[i] = input()
words = []
words_num = int(input())
for i in range(words_num):
    words.append(input())

found_words = []

reverse_words = []
for word in words:
    reverse_words.append(word[::-1])


for word in words:
    found_word = False
    for y in range(rows):
        for x in range(columns):
            if board[y][x] != word[0]:
                continue
            i = 0
            while True: #right dir
                i += 1
                if x + i == columns: #hit wall
                    break
                if board[y][x + i] != word[i]: #word not found
                    break
                if board[y][x + i] == word[len(word) - 1]: #reached end of word
                    found_word = True
                    break
            i = 0
            while True: #down dir
                i += 1
                if y + i == rows: #hit wall
                    break
                if board[y + i][x] != word[i]: #word not found
                    break
                if board[y + i][x] == word[len(word) - 1]: #reached end of word
                    found_word = True
                    break
            i = 0
            while True: #right-down dir
                i += 1
                if x + i == columns or y + i == rows: #hit wall
                    break
                if board[y + i][x + i] != word[i]: #word not found
                    break
                if board[y + i][x + i] == word[len(word) - 1]: #reached end of word
                    found_word = True
                    break
            i = 0
            while True: #right-up dir
                i += 1
                if x + i == columns or y - i == -1: #hit wall
                    break
                if board[y - i][x + i] != word[i]: #word not found
                    break
                if board[y - i][x + i] == word[len(word) - 1]: #reached end of word
                    found_word = True
                    break
            if found_word == True:
                found_words.append(word)
                break
        if found_word == True:
            found_word = False
            break

for word in reverse_words:
    found_word = False
    for y in range(rows):
        for x in range(columns):
            if board[y][x] != word[0]:
                continue
            i = 0
            while True: #right dir
                i += 1
                if x + i == columns: #hit wall
                    break
                if board[y][x + i] != word[i]: #word not found
                    break
                if board[y][x + i] == word[len(word) - 1]: #reached end of word
                    found_word = True
                    break
            i = 0
            while True: #down dir
                i += 1
                if y + i == rows: #hit wall
                    break
                if board[y + i][x] != word[i]: #word not found
                    break
                if board[y + i][x] == word[len(word) - 1]: #reached end of word
                    found_word = True
                    break
            i = 0
            while True: #right-down dir
                i += 1
                if x + i == columns or y + i == rows: #hit wall
                    break
                if board[y + i][x + i] != word[i]: #word not found
                    break
                if board[y + i][x + i] == word[len(word) - 1]: #reached end of word
                    found_word = True
                    break
            i = 0
            while True: #right-up dir
                i += 1
                if x + i == columns or y - i == -1: #hit wall
                    break
                if board[y - i][x + i] != word[i]: #word not found
                    break
                if board[y - i][x + i] == word[len(word) - 1]: #reached end of word
                    found_word = True
                    break
            if found_word == True:
                found_words.append(word[::-1])
                break
        if found_word == True:
            found_word = False
            break

for word in words:
    if word in found_words:
        print(f"{word} FOUND")
    else:
        print(f"{word} NOT FOUND")