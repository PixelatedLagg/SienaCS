x = [int(num) for num in str(input()).split(' ')]
times = {0:0, 1:0, 2:0}

def dist(n1, n2):
    if x[(2 * n1) - 1] > x[(2 * n2) - 1]:
        return f"{n2} {n1}"
    if x[(2 * n1) - 1] < x[(2 * n2) - 1]:
        return f"{n1} {n2}"
    if n1 > n2:
        return f"{n2} {n1}"
    return f"{n1} {n2}"

for i in range(3):
    times[i] = (100 - x[(2 * i) + 1]) / x[2 * i]

if times[0] == times[1] and times[0] == times[2]:
    if x[1] == x[3] and x[1] == x[5]:
        print("1 2 3")
        exit()

    if x[1] == x[3]:
        if x[5] > x[1]:
            print("3 1 2")
        else:
            print("1 2 3")
    if x[1] == x[5]:
        if x[3] > x[1]:
            print("2 1 3")
        else:
            print("1 3 2")
    if x[3] == x[5]:
        if x[1] > x[3]:
            print("1 2 3")
        else:
            print("2 3 1")
    exit()

if times[0] == times[1]:
    if times[2] > times[0]:
        print(f"{dist(1, 2)} 3")
        exit()
    else:
        print(f"3 {dist(1, 2)}")
        exit()

if times[0] == times[2]:
    if times[1] > times[0]:
        print(f"{dist(1, 3)} 2")
        exit()
    else:
        print(f"2 {dist(1, 3)}")
        exit()

if times[1] == times[2]:
    if times[0] > times[1]:
        print(f"{dist(2, 3)} 1")
        exit()
    else:
        print(f"1 {dist(2, 3)}")
        exit()

times_final = list(times.values())
result = []


while len(times_final) != 0:
    for i in range(3):
        if len(times_final) == 0:
            break
        if min(times_final) == times[i]:
            result.append(i)
            times_final.remove(min(times_final))
print(f"{result[0] + 1} {result[1] + 1} {result[2] + 1}")