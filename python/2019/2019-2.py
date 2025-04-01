n = int(input())
n_str = list(str(n))
steps = 0
sum = n

while sum != 1 and sum != 89:
    sum = 0
    for char in n_str:
        sum += int(char) * int(char)
    n_str = list(str(sum))
    steps += 1

if sum == 1:
    print(f"1 {steps}")

if sum == 89:
    print(f"89 {steps}")