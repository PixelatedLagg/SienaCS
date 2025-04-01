import math

num = int(input())
arr = [0] * num
for i in range(num):
    arr[i] = i

def shuffle(_arr):
    split = 0
    if len(_arr) % 2 == 0:
        split = math.floor(len(_arr) / 2)
    else:
        split = math.floor(len(_arr) / 2) + 1
    _arr_1 = _arr[0:split]
    _arr_2 = _arr[split:len(_arr)]
    new_arr = [0] * len(arr)
    for i in range(len(_arr_1)):
        new_arr[i * 2] = _arr_1[i]
    for i in range(len(_arr_2)):
        new_arr[(i * 2) + 1] = _arr_2[i]
    return new_arr

count = 1
test = shuffle(arr)

while test != arr:
    count += 1
    test = shuffle(test)

print(count)