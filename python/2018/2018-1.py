word = list(str(input()))
length = int(input())
for i in range(length):
    word[int(input()) - 1] = ''
print(''.join(word))