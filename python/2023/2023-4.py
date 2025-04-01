num_students = int(input())
num_elim = int(input())
remaining = [True] * num_students #students still in

if num_elim >= num_students:
    remaining[num_elim % num_students - 1] = False
    position = num_elim % num_students - 1
else:
    remaining[num_elim - 1] = False
    position = num_elim - 1

for repeat in range(num_students - 3):
    temp = num_elim
    while temp != 0:
        if position == num_students - 1:
            position = 0
        else:
            position += 1
        if remaining[position] == True:
            temp -= 1
    remaining[position] = False

winners = []
for i in range(num_students):
    if remaining[i] == True:
        winners.append(i + 1)

print(f"{winners[0]} {winners[1]}")