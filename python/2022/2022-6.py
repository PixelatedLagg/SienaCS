target = int(input())
num_lines = int(input())
line_stops = []
for i in range(num_lines):
    input()
    line_stops.append(list(map(int, input().split(' '))))
count = 0

def move(current_line, index, alreadyMovedLines):
    global count
    if line_stops[current_line][-1] == index:
        if index == target: #done!
            count += 1
        return #dead end!
    if index in line_stops[current_line] and not alreadyMovedLines:
        for i in range(len(line_stops)):
            if i == current_line:
                continue
            if index in line_stops[i]:
                move(i, index, True) #get off
    move(current_line, index + 1, False) #stay on

for i in range(len(line_stops)):
    if 1 in line_stops[i]: #ensure not skipping over invalid move
        move(i, 2, False)

print(count)