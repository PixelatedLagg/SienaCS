import math

i, j = map(int, input().split(' '))
i -= 1
j -= 1
print(f"1/{int((i + 1) * (math.factorial(i)/(math.factorial(j) * math.factorial(i - j))))}")