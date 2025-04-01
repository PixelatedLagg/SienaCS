num_coins = int(input())
coins = []
for read_input in range(1, num_coins + 1):
    coins.append(int(input()))
change = int(input())
addition = []

dp = [change + 1] * (change + 1)
dp[0] = 0

coin_path = [[] for initialize in range(change + 1)]
coin_path[0] = []

for a in range(1, change + 1):
    for coin in coins:
        if a - coin >= 0:
            if (dp[a] > 1 + dp[a - coin]):
                coin_path[a] = coin_path[a - coin].copy()
                coin_path[a].append(coin)
                dp[a] = 1 + dp[a - coin]

format = []
coin_path[change].sort(reverse = True)
for val in coin_path[change]:
    format.append(str(val))
    format.append(' + ')
format.pop()

print(f"{change} = {''.join(format)}")
print(f"{dp[change]} coins required")