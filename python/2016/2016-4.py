a = int(input())
b = int(input())

def getMp(num):
    temp = num
    remaining = num
    steps = 0
    while remaining > 9:
        remaining = 1
        for c in str(temp):
            remaining *= int(c)
        temp = remaining
        steps += 1
    return steps

def getMdr(num):
    temp = num
    remaining = num
    while remaining > 9:
        remaining = 1
        for c in str(temp):
            remaining *= int(c)
        temp = remaining
    return remaining

freq = [0] * 10
largestMp = 0
largestMpNumber = 0
for i in range(b, a - 1, -1): #iterate backwards
    mp = getMp(i)
    if mp >= largestMp:
        largestMp = mp
        largestMpNumber = i
    freq[getMdr(i)] += 1

print(a)
print(b)
print(f"{largestMp} {largestMpNumber}")
for i in range(10):
    print(f"{i} {freq[i]}")