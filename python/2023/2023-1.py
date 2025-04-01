import math

upper = int(input())
pow = 0
while (math.pow(2, pow) <= upper):
    print(int(math.pow(2, pow)))
    pow += 1