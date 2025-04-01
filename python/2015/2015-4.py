current = int(input())

def newNumber(s):
    top = []
    bottom = []
    for c in str(s):
        top.append(int(c))
        bottom.append(int(c))
    top = list(map(str, sorted(top)))
    bottom = list(map(str, sorted(bottom, reverse=True)))
    return abs(int(int(''.join(top)) - int(''.join(bottom))))


steps = 1
previous_nums = []

while not newNumber(current) in previous_nums:
    steps += 1
    current = newNumber(current)
    previous_nums.append(current)

print(steps)