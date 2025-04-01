import copy

a, b = map(int, input().split(' '))
years = {}

def scubey(s, i, t, path):
    global years
    if s > t:
        return #dead end!
    if s == t:
        years.update({t : path})
        return #scubey!
    if i < 100:
        scubey(s, i + 1, t, path) #skip index
    newPath = copy.deepcopy(path)
    newPath.append(i)
    scubey(s + (i * i * i), i + 1, t, newPath) #add index
    return #dead end!

def getScubeyType(arr, i):
    if len(arr) == arr[-1] - arr[0] + 1:
        if arr[0] == 1: #perfect
            if i < 10:
                print(f" {i} Perfect {arr[0]} {arr[-1]}")
            else:
                print(f"{i} Perfect {arr[0]} {arr[-1]}")
        else: #normal
            if i < 10:
                print(f" {i} Normal  {arr[0]} {arr[-1]}")
            else:
                print(f"{i} Normal  {arr[0]} {arr[-1]}")
    if len(arr) == arr[-1] - arr[0]: #near
        start = arr[0]
        for j in range(len(arr)):
            if arr[j] != start + j:
                if i < 10:
                    print(f" {i} Near    {arr[0]} {arr[-1]} {j + 1}")
                else:
                    print(f"{i} Near    {arr[0]} {arr[-1]} {j + 1}")
                return


for i in range(a, b + 1):
    scubey(0, 1, i, [])

for y in years.keys():
    getScubeyType(years[y], y)