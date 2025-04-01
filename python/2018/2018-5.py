num_cards = int(input())
cards = []
for i in range(num_cards):
    cards.append(input())
matches = []

include = []
exclude = []
for i in cards:
    for j in cards:
        for k in cards:
            if i == j or j == k: #no duplicates
                continue
            reject = False
            for x in range(4):
                if (i[x] == j[x] and j[x] == k[x]): #all same property
                    continue
                if (i[x] != j[x] and j[x] != k[x] and i[x] != k[x]): #all different properties
                    continue
                reject = True
            if reject == True:
                continue
            result = [str(i), str(j), str(k)]
            matches.append(sorted(result))
                


if len(matches) == 0:
    print("NO SETS")
    exit()
print("OUT")
matches = sorted([list(t) for t in {tuple(sub) for sub in matches}])
for m in matches:
    print(m)