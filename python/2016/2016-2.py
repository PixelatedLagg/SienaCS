x = int(input())
current = 1
count = 1
for i in range(2, x):
    if (current == x):
        print(count)
        break
    if (current > x):
        print("0")
        break
    current += i
    count += 1