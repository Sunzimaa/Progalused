import datetime
from datetime import date
isikukood = input("Sisestage oma isikukood: ")

isikukood.splitlines()
aasta = (isikukood[1:3])
kuu = int(isikukood[3:5])
päev = int(isikukood[5:7])



print("Sünni aasta on " + str(aasta) + ", sünni5kuupäev on " + str(päev) + "." + str(kuu) + ".")
todays_date = date.today()
praegune = todays_date
praegu_aasta = str(todays_date.year)[2:4]

sugu = int(isikukood[0:1])
if sugu == 1:
    print("Sugu on: Mees")
elif sugu == 2:
    print("Sugu on: Naine")
elif sugu == 3:
    print("Sugu on: Mees")
elif sugu == 4:
    print("Sugu on: Naine")
elif sugu == 5:
    print("Sugu on: Mees")
elif sugu == 6:
    print("Sugu on: Naine")


a = (int(aasta))
b = int(praegu_aasta)

if a>b:
    age = b-a+100
else:
    age = b-a

print(f"Vanus on: {age}")