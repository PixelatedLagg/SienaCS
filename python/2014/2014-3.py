import math

lower = int(input())
upper = int(input())

hyps = [5,13,10,25,17,15,41,26,61,20,37,50,39,34,65,30,29,52,35,75,40,51,74,45,53,78,68,55,60,58,70,73,80,85,90,87,97]

days = 0
list_of_days = []
for x in range(lower - 2000, upper - 1999):
    if (not int(x) in hyps):
        continue
    for m in range(1, 72):
        for d in range(1, 72):
            if (m * m + d * d == x * x):
                days += 1
                list_of_days.append((m, d, x))

print(days)
for day in list_of_days:
    print(f"{day[0]}-{day[1]}-{day[2]}")