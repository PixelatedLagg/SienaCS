length = int(input())
before = str(input())
after = str(input())

def index_loop(x):
    if x < length:
        return x
    return (x % length)

if (before == after):
    print("CYCLE")
    exit()

offset = 0
for i in range(0, length):
    if (after[i] == before[0]):
        offset = i

for i in range(0, length):
    if (before[i] != after[index_loop(i + offset)]):
        print("NO CYCLE")
        exit()
print("CYCLE")