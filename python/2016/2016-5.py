import copy

n = int(input())
count = 0

def add(s, i):
    global count
    if len(s) == 0:
        newS = copy.deepcopy(s)
        newS.append(i)
        add(newS, i + 1)
    else:
        if s[len(s) - 1] == 9: #done!
            if eval(''.join(map(str, s))) == n:
                count += 1
            return
        if s[len(s) - 1] == '+' or s[len(s) - 1] == '-':
            newS = copy.deepcopy(s)
            newS.append(i)
            add(newS, i + 1)
        else:
            newS = copy.deepcopy(s)
            newS.append(i)
            add(newS, i + 1)
            newS = copy.deepcopy(s)
            newS.append('-')
            add(newS, i)
            newS = copy.deepcopy(s)
            newS.append('+')
            add(newS, i)
    return #dead end!

add([], 1)
print(n)
print(count)