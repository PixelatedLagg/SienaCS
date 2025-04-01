k = int(input())
board = []
for i in range(k):
    board.append(input())

words = []
num_words = int(input())
found_words = {}
for i in range(num_words):
    w = input()
    words.append(w)
    found_words.update({w : 0})

found_word_coords = []
directions = [
    (1, 0), (0, 1), (1, 1), (-1, 1)
]
reverse_words = []

for word in words:
    reverse_words.append(word[::-1])

def inBounds(a, b):
    return -1 < a and a < k and -1 < b and b < k

for i in range(k):
    for j in range(k):
        for dir in directions:
            for word in words:
                offset = 0
                while inBounds(i + dir[0] * offset, j + dir[1] * offset) and board[i + dir[0] * offset][j + dir[1] * offset] == word[offset]:
                    offset += 1
                    if offset == len(word): #found word!
                        found_words[word] += 1
                        found_word_coords.append([i, j, i + dir[0] * offset, j + dir[1] * offset])
                        break
            for word in reverse_words:
                offset = 0
                while inBounds(i + dir[0] * offset, j + dir[1] * offset) and board[i + dir[0] * offset][j + dir[1] * offset] == word[offset]:
                    offset += 1
                    if offset == len(word): #found word!
                        if not [i, j, i + dir[0] * offset, j + dir[1] * offset] in found_word_coords:
                            found_words[word[::-1]] += 1
                        break

for k in found_words.keys():
    print(f"{k}:{found_words[k]}")