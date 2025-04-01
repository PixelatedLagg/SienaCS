x = int(input())
y = int(input())
total = 0
while x > 0 and y > 0:
    total += x * y
    x -= 1
    y -= 1
print(total)