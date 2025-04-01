import math

word = input()
left_sub = word[0:int(len(word)/2)]
right_sub = word[int(len(word)/2):int(len(word))]
if len(word) % 2 == 1:
    left_sub = word[0:int(math.floor(len(word)/2))]
    right_sub = word[int(math.floor(len(word)/2) + 1):(len(word))]

left_dict = {}
right_dict = {}

for i in range(27):
    left_dict.update({chr(ord('A') + i) : 0})
    right_dict.update({chr(ord('A') + i) : 0})

for i in range(len(left_sub)):
    left_dict[left_sub[i]] += 1
    right_dict[right_sub[i]] += 1

bal = 0
left = 0
right = 0
for i in range(27):
    if left_dict[chr(ord('A') + i)] == right_dict[chr(ord('A') + i)]:
        bal += 1
    if left_dict[chr(ord('A') + i)] > right_dict[chr(ord('A') + i)]:
        left += 1
    if left_dict[chr(ord('A') + i)] < right_dict[chr(ord('A') + i)]:
        right += 1

print(word)
if left + right == 0:
    print("PERFECTLY BALANCED")
    exit()

if left > right:
    print("LEFT UNBALANCED")
    exit()

if left < right:
    print("RIGHT UNBALANCED")
    exit()

if left == right:
    print("BALANCED")