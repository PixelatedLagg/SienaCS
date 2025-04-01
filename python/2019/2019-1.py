input_ = str(input()).split(' ')
n = int(input_[0])
s = str(input_[1])
t = str(input_[2])

base_s:int = 0 #in teaspoons

match s:
    case "TEASPOONS":
        base_s = n
    case "TABLESPOONS":
        base_s = n * 3
    case "CUPS":
        base_s = n * 48
    case "PINTS": 
        base_s = n * 96
    case "QUARTS":
        base_s = n * 192
    case _: #gallons
        base_s = n * 768

match t:
    case "TEASPOONS":
        print(base_s)
    case "TABLESPOONS":
        print(int(base_s / 3))
    case "CUPS":
        print(int(base_s / 48))
    case "PINTS": 
        print(int(base_s / 96))
    case "QUARTS":
        print(int(base_s / 192))
    case _: #gallons
        print(int(base_s / 768))