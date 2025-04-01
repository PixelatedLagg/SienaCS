speed = int(input())
str_ = str(input())
if speed == 0:
    print("CALM")
    exit()

if (str_[0] == "K"): #knots
    if speed >= 1 and speed <= 3:
        print("LIGHT-AIR")
        exit()
    if speed >= 4 and speed <= 6:
        print("LIGHT-BREEZE")
        exit()
    if speed >= 7 and speed <= 10:
        print("GENTLE-BREEZE")
        exit()
    if speed >= 11 and speed <= 16:
        print("MODERATE-BREEZE")
        exit()
    if speed >= 17 and speed <= 21:
        print("FRESH-BREEZE")
        exit()
    if speed >= 22 and speed <= 27:
        print("STRONG-BREEZE")
        exit()
    if speed >= 28 and speed <= 33:
        print("NEAR-GALE")
        exit()
    if speed >= 34 and speed <= 40:
        print("GALE")
        exit()
    if speed >= 41 and speed <= 47:
        print("SEVERE-GALE")
        exit()
    if speed >= 48 and speed <= 55:
        print("STORM")
        exit()
    if speed >= 56 and speed <= 63:
        print("VIOLENT-STORM")
        exit()
    if speed >= 64:
        print("HURRICANE")
        exit()
else:
    if speed >= 1 and speed <= 3:
        print("LIGHT-AIR")
        exit()
    if speed >= 4 and speed <= 7:
        print("LIGHT-BREEZE")
        exit()
    if speed >= 8 and speed <= 12:
        print("GENTLE-BREEZE")
        exit()
    if speed >= 13 and speed <= 18:
        print("MODERATE-BREEZE")
        exit()
    if speed >= 19 and speed <= 24:
        print("FRESH-BREEZE")
        exit()
    if speed >= 25 and speed <= 31:
        print("STRONG-BREEZE")
        exit()
    if speed >= 32 and speed <= 38:
        print("NEAR-GALE")
        exit()
    if speed >= 39 and speed <= 46:
        print("GALE")
        exit()
    if speed >= 47 and speed <= 54:
        print("SEVERE-GALE")
        exit()
    if speed >= 55 and speed <= 63:
        print("STORM")
        exit()
    if speed >= 64 and speed <= 72:
        print("VIOLENT-STORM")
        exit()
    if speed >= 73:
        print("HURRICANE")
        exit()