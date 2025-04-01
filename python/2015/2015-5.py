top = int(input())
bottom = int(input())
top_str = str(top)
bottom_str = str(bottom)
width = 0

if (len(str(top * bottom)) >= max(len(top_str), len(bottom_str)) + 1):
    width = len(str(top * bottom))
else:
    width = max(len(top_str), len(bottom_str)) + 1

def format(string):
    if len(string) == width:
        return string
    else:
        return f"{''.join([' '] * (width - len(string)))}{string}"

def multiplyformat(a, b, i):
    if a * b == 0:
        return ''.join(['0'] * i)
    return a * b

print(' ' + format(top_str))
print(' ' + f"x{''.join([' '] * (width - len(bottom_str) - 1))}{bottom_str}")
print(' ' + ''.join(['-'] * width))
if len(bottom_str) > 1 and len(top_str) > 1:
    for digit in range(len(bottom_str)):
        print(' ' + format(str(multiplyformat(int(bottom_str[len(bottom_str) - digit - 1]), top, len(top_str))) + ''.join(['0'] * digit)))
    print(' ' + ''.join(['-'] * width))
print(' ' + format(str(top * bottom)))