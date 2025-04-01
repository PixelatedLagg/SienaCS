a = int(input()) #seconds
started = False

#more than one year
if a % 31536000 < a:
    years = int((a - (a % 31536000)) / 31536000)
    print(f"{years} years")
    a -= years * 31536000
    started = True

#more than one day
if a % 86400 < a or started:
    days = int((a - (a % 86400)) / 86400)
    print(f"{days} days")
    a -= days * 86400
    started = True

#more than one hour
if a % 3600 < a or started:
    hours = int((a - (a % 3600)) / 3600)
    print(f"{hours} hours")
    a -= hours * 3600
    started = True
    
#more than one minute
if a % 60 < a or started:
    minutes = int((a - (a % 60)) / 60)
    print(f"{minutes} minutes")
    a -= minutes * 60

if a > 0:
    print(f"{int(a)} seconds")