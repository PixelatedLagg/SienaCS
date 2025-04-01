import copy

n = int(input())

intersections = []
vert_lines = {}
horiz_lines = {}
max_val = 0

def inBounds(a, b, x):
    return x >= a and b >= x

def checkOverlapping(arr):
    arr.sort()
    merged = [arr[0]]
    for start, end in arr[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged

def hasSegment(a, b, arr):
    for x in arr:
        if inBounds(x[0], x[1], a) and inBounds(x[0], x[1], b):
            return True
    return False

for i in range(n):
    i1, j1, i2, j2 = map(int, input().split(' '))
    max_val = max(i1, j1, i2, j2, max_val)
    if (i1 == i2): #vertical line
        if not i1 in horiz_lines.keys():
            horiz_lines.update({i1:[sorted((j1, j2))]})
        else:
            temp = copy.deepcopy(horiz_lines[i1])
            temp.append(sorted((j1, j2)))
            horiz_lines[i1] = checkOverlapping(temp)
    if (j1 == j2):
        if not j1 in vert_lines.keys():
            vert_lines.update({j1:[sorted((i1, i2))]})
        else:
            temp = copy.deepcopy(vert_lines[j1])
            temp.append(sorted((i1, i2)))
            vert_lines[j1] = checkOverlapping(temp)

count = 0
for i in range(max_val + 1):
    for j in range(max_val + 1):
        offset = 1
        while i - offset >= 0 and j + offset < max_val + 1:
            if not j in vert_lines.keys() or not j + offset in vert_lines.keys() or not i - offset in horiz_lines.keys() or not i in horiz_lines.keys():
                offset += 1
                continue
            if hasSegment(j, j + offset, horiz_lines[i]) and hasSegment(j, j + offset, horiz_lines[i - offset]) and hasSegment(i - offset, i, vert_lines[j]) and hasSegment(i - offset, i, vert_lines[j + offset]):
                count += 1
            offset += 1
print(count)