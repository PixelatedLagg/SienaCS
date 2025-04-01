import math

def supersum(x):
    return int((x * (x + 1) / 2) + (x * (x + 1) * (2 * x + 1) / 6) + math.pow((x * (x + 1) / 2), 2))

a = int(input())

print(supersum(a))