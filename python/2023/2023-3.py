dice = [0] * 5
for i in range(5):
    dice[i] = int(input())
s_dice = sorted(dice)
check = True

for i in range(5):
    if (s_dice[i] != s_dice[0] + i):
        check = False
if check == True:
    print(sum(dice) + 500)
    exit()

storedThreeKind = 0
storedTwoKind = 0
matches = 0

for val in range(1, 7):
    for i in range(5):
        if dice[i] == val:
            matches += 1
    if matches == 5:
        print(5 * val + 1000)
        exit()
    if matches == 4:
        print(4 * val + 600)
        exit()
    if matches == 3:
        if storedTwoKind != 0: #full house
            print(sum(dice) + 400)
            exit()
        else:
            storedThreeKind = val
        continue
    if matches == 2:
        if storedThreeKind != 0: #full house
            print(sum(dice) + 400)
            exit()
        if storedTwoKind != 0: #two pair
            print(storedTwoKind * 2 + val * 2 + 200)
            exit()
        storedTwoKind = val
    matches = 0

if storedTwoKind != 0: #one pair
    print(storedTwoKind * 2 + 100)
    exit()
if storedThreeKind != 0:
    print(storedThreeKind * 3 + 300)
print(sum(dice))