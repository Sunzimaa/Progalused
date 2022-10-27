nimi = str(input("Sisestage oma nimi: "))
lubatud = str(input("Sisestage lubatud kiirus km/h: "))
tegelik = str(input("Sisestage tegelik kiirus km/h: "))
summa = (int(tegelik) - int(lubatud)) * 3
summa = min(summa, 190)
print(f"{nimi}, kiiruse ületamise eest on trahv {summa} eurot")


