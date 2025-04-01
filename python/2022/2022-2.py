titles = {"MARSHAL": 9,"GENERAL": 8,"COLONEL": 7,"MAJOR": 6,"CAPTAIN": 5,"LIEUTENANT": 4,"SERGEANT": 3,"MINER": 2,"SCOUT": 1,"SPY": 0}

attack = str(input())
defend = str(input())

if defend == "FLAG":
    print('FLAG REMOVED')
    exit()

if defend == "BOMB" and attack != "MINER":
    print(f"{attack} REMOVED")
    exit()

if defend == "BOMB" and attack == "MINER":
    print("BOMB REMOVED")
    exit()

if defend == "MARSHAL" and attack == "SPY":
    print("MARSHAL REMOVED")
    exit()

if defend == attack:
    print("BOTH REMOVED")
    exit()

if titles[defend] > titles[attack]:
    print(f"{attack} REMOVED")
else:
    print(f"{defend} REMOVED")