num = int(input())

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

found = False
for base in range(2, 17):
    converted = "".join(str(d) if d < 10 else chr(ord('A') + d - 10) for d in numberToBase(num, base))
    if len(set(converted)) == 1:
        found = True
        print(f"{num} Base {base}: {converted}")

if found == False:
    print("NO")