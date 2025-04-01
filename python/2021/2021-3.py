num_str = str(input())
target = len(num_str)
num = int(num_str)

answer = []

while num > 0:
    if num >= 1000:
        answer.append("M")
        num -= 1000
        continue
    if num >= 900:
        answer.append("CM")
        num -= 900
        continue
    if num >= 500:
        answer.append("D")
        num -= 500
        continue
    if num >= 400:
        answer.append("CD")
        num -= 400
        continue
    if num >= 100:
        answer.append("C")
        num -= 100
        continue
    if num >= 90:
        answer.append("XC")
        num -= 90
        continue
    if num >= 50:
        answer.append("L")
        num -= 50
        continue
    if num >= 40:
        answer.append("XL")
        num -= 40
        continue
    if num >= 10:
        answer.append("X")
        num -= 10
        continue
    if num >= 9:
        answer.append("IX")
        num -= 9
        continue
    if num >= 5:
        answer.append("V")
        num -= 5
        continue
    if num >= 4:
        answer.append("IV")
        num -= 4
        continue
    if num >= 1:
        answer.append("I")
        num -= 1
        continue

if len(''.join(answer)) == target:
    print(f"{''.join(answer)} ROMAN-EQUIVALENT")
else:
    print(f"{''.join(answer)} NOT ROMAN-EQUIVALENT")