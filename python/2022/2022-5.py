'''
index=HAT, SHIRT, PANTS, SOCKS
value=GREEN, RED, BLUE, YELLOW
'''

table = [[0, 0, 0, 0] for i in range(256)]
count = 0
for hat in range(4):
    for shirt in range(4):
        for pants in range(4):
            for socks in range(4):
                table[count] = [hat, shirt, pants, socks]
                count += 1

def convertItem(item):
    if item == "HAT":
        return 0
    if item == "SHIRT":
        return 1
    if item == "PANTS":
        return 2
    if item == "SOCKS":
        return 3

def convertValue(val):
    if val == "GREEN":
        return 0
    if val == "RED":
        return 1
    if val == "BLUE":
        return 2
    if val == "YELLOW":
        return 3

num_restrict = int(input())
for i in range(num_restrict):
    input_array = input().split(' ')
    index1 = convertItem(input_array[1])
    val1 = convertValue(input_array[0])
    index2 = convertItem(input_array[3])
    val2 = convertValue(input_array[2])
    for i in range(256):
        if (table[i][index1] == val1 and table[i][index2] == val2): #hit!
            table[i][0] = -1

c = 0
for i in range(256):
    if table[i][0] != -1:
        c += 1
print(c)