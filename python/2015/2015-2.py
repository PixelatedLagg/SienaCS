cards = list(map(int, input().split()))
copy_cards = cards.copy()

if min(cards) == max(cards):
    print("Four-of-a-Kind")
    exit()

copy_cards.remove(max(copy_cards))

if min(copy_cards) == max(copy_cards):
    print("Three-of-a-Kind")
    exit()

copy_cards = cards.copy()
copy_cards.remove(min(copy_cards))

if min(copy_cards) == max(copy_cards):
    print("Three-of-a-Kind")
    exit()

for i in range(0, 4):
    for j in range(0, 4):
        if (i == j):
            continue
        if (cards[i] == cards[j]):
            del cards[i]
            del cards[j - 1]
            if cards[0] == cards[1]:
                print("Two-Pairs")
            else:
                print("One-Pair")
            exit()
print("No-Matches")
