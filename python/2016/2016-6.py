import copy
import math

k, c = map(int, input().split(' '))

if k == 1 or k == 2:
    print(c)
    exit()

dp = [[-1] * (k + 1) for i in range(k + 1)]
dp[3] = [c, 0, 0]

def populate(index):
    if dp[index][0] != -1:
        return dp[index]
    temp = copy.deepcopy(populate(index - 1))
    sum = 0
    concede = []
    break_ = False
    votes_needed = (index / 2)
    if index % 2 == 1:
        votes_needed = math.ceil(index / 2) - 1
    print(f"VOTES{votes_needed}")
    for num in range(c):
        for i in range(len(temp)):
            if temp[i] == num:
                print(num)
                if len(concede) == votes_needed:
                    break_ = True
                    break
                concede.append((i, num + 1))
                sum += num + 1
        if break_:
            break
    print(concede)
    answer = [0] * index
    answer[0] = c - sum
    for t in concede:
        answer[t[0] + 1] = t[1]
    dp[index] = answer
    return answer

print(*populate(k))