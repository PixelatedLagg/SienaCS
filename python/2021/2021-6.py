import copy

n = int(input())
combos = []

def add(s, i):
    global combo
    if i == 10: #found combo!
        if (eval(''.join(map(str, s))) == n):
            combos.append(''.join(map(str, s)))
        return
    if len(s) == 0:
        newS = copy.deepcopy(s)
        newS.append(i)
        add(newS, i + 1)
    else:
        if s[len(s) - 1] == '-' or s[len(s) - 1] == '+':
            newS = copy.deepcopy(s)
            newS.append(i)
            add(newS, i + 1)
        else:
            newS = copy.deepcopy(s)
            newS.append('+')
            add(newS, i)
            newS = copy.deepcopy(s)
            newS.append('-')
            add(newS, i)
            newS = copy.deepcopy(s)
            newS.append(i)
            add(newS, i + 1)
    return #dead end!

add([], 1)
combos.sort(key = lambda s: list(map(int, s.replace("-","+").split("+"))))
if len(combos) == 0:
    print("NO SOLUTIONS FOUND")
else:
    for c in combos:
        print(c)