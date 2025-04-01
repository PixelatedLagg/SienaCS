x = int(input())
steps = 0
val = x
while val != 1:
    if val % 2 == 0:
        val /= 2
    else:
        val = (val * 3) + 1
    steps += 1
print(f"{x} {steps}")