import math

lower = int(input())
upper = int(input())

def check(x, y, z):
    return x + y > z and y + z > x and x + z > y

def sort_lowest(list_old):
    new_list = []
    new_list.append(min(list_old))
    list_old.remove(min(list_old))
    new_list.append(min(list_old))
    list_old.remove(min(list_old))
    new_list.append(min(list_old))
    return new_list

for x in range(lower, upper + 1):
    tri = 0
    tri_combos = []
    for i in range(1, x):
        for j in range(1, x):
            for k in range(1, x):
                if (i + j + k == x and check(i, j, k)):
                    current_combo = sort_lowest([i, j, k])
                    if (not current_combo in tri_combos):
                        tri_combos.append(current_combo)
                        tri += 1
    print(f"{x} {tri}")