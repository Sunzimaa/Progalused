

print("Sisestage oma nimi")
name = input()
print(f"Tere {name}")

print("Sisestage lubatud kiirus km/h")
kiirus = int(input())
print(f"Lubatud kiirus on {kiirus} km/h")

print("Sisestage tegelik kiirus km/h")
kiirus2 = int(input())
print(f"Tegelik kiirus on {kiirus2} km/h")

#trahv = min(80, 190)
#if kiirus > kiirus2:
#    print(f"{name}, kiiruse ületamise eest on trahv {trahv} eurot")
#kiirus < kiirus2:
#    print(f"{name}, kõik on korras!")


trahv = min(80, 190)
if kiirus > kiirus2:
    trahv = (kiirus - kiirus2) * 3
    print(f"{name}, kiiruse ületamise eest on trahv {trahv} eurot")


