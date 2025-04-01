num_players = int(input())
lockers = list(map(int, input().split(' ')))

def find_in_locker(target, locker):
    index = locker
    currentCount = 0
    while (lockers[index] != target):
        currentCount += 1
        index = lockers[index] - 1
    return currentCount

results = []
for i in range(0, num_players):
    results.append(find_in_locker(i + 1, i))

results.sort()

print(f"{results[num_players - 1] + 1} {results[0] + 1}")