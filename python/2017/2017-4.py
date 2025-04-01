str_1 = list(map(int, str(input()).split(' ')))
del str_1[len(str_1) - 1]
str_2 = list(map(int, str(input()).split(' ')))
del str_2[len(str_2) - 1]

offset = 0
for j in range(len(str_1)):
    if str_1[0] == str_2[j]:
        offset = j

def wrap_around(i, length):
    if i > length - 1:
        return i - length
    else:
        return i
correct = True
for i in range(len(str_1)):
    if str_1[i] != str_2[wrap_around(i + offset, len(str_2))]:
        correct = False
        break

if correct == True and len(str_1) == len(str_2):
    print("CYCLE")
else:
    print("NOCYCLE")