import math

h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

td1 = h1 + (m1 / 60)
td2 = h2 + (m2 / 60)

td3 = 0
if (td1 > td2):
    td3 = 24 - td1 + td2
else:
    td3 = td2 - td1
print(f"{math.floor(td3)} {round((td3 - math.floor(td3)) * 60)}")