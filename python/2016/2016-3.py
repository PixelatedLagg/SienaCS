a = int(input())
b = int(input())

dp = [[] for _ in range(b + 1)]
dp[1] = []

def getFactors(num):
    if num == 1:
        return []
    if len(dp[num]) != 0:
        return dp[num]
    for i in range(num, 1, -1): #iterate from top to bottom
        if num % i == 0:
            dp[num].append(i)
            dp[num].append(int(num / i))
            dp[num].extend(getFactors(int(num / i)))
            dp[num].extend(getFactors(i))
    dp[num] = list(set(dp[num])) #get rid of duplicates
    return dp[num]


perfect = 0
abundant = 0
deficient = 0
for i in range(a, b + 1):
    if i == 1:
        deficient += 1
        continue
    s = sum(getFactors(i)) - i
    if s == i:
        perfect += 1
    if s < i:
        deficient += 1
    if s > i:
        abundant += 1

print(a)
print(b)
print(perfect)
print(abundant)
print(deficient)