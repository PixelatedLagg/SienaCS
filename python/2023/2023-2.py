lower = int(input())
upper = int(input())
k = int(input())
solution = False
for i in range(lower, upper + 1):
    steps = 0
    x = i
    while x != 1:
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1
        steps += 1
    if steps == k:
        solution = True
        print(i)

if solution == False:
    print("None")