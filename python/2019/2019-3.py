import math

input_array = str(input()).split(' ')
n = int(input_array[0])
b = int(input_array[1])
char_const = ord('A')
answer = []
div = n

while div != 0:
    answer.append(str(div % b))
    print(f"{math.floor(div / b)} {div % b}")
    div = math.floor(div / b)

for i in range(len(answer)):
    if int(answer[i]) > 9:
        answer[i] = chr(char_const + int(answer[i]) - 10)

reverse = answer[::-1]
print(''.join(reverse))