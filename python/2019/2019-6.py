import itertools

everything = input()
add1, add2, sum_ = everything.split(' ')
chars = list(dict.fromkeys(everything.replace(' ', '')))

if len(chars) > 10:
    print("NO SOLUTION")
    exit()

sol_add1, sol_add2, sol_sum = [], [], []

for assignment in itertools.permutations(range(10), len(chars)):
    mapping = dict(zip(chars, assignment))

    if mapping[add1[0]] == 0 or mapping[add2[0]] == 0 or mapping[sum_[0]] == 0: #no leading zeroes
        continue

    int_add1 = int(''.join(str(mapping[ch]) for ch in add1))
    int_add2 = int(''.join(str(mapping[ch]) for ch in add2))
    int_sum = int(''.join(str(mapping[ch]) for ch in sum_))

    if int_add1 + int_add2 == int_sum:
        sol_add1.append(int_add1)
        sol_add2.append(int_add2)
        sol_sum.append(int_sum)

if sol_add1:
    min_solution = min(zip(sol_add1, sol_add2, sol_sum))
    print(*min_solution)
else:
    print("NO SOLUTION")