def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

input_str = str(input())
a_ = int(input_str, 2)
b_ = int('1' * len(input_str), 2)
gcd_ = gcd(a_, b_)

print(f"{int(a_ / gcd_)}/{int(b_ / gcd_)}")