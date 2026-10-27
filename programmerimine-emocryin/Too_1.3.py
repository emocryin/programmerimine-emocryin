from calendar import *
from datetime import *
from math import *

tana = date.today()
print("Tere! \nTäna on",tana)

kys = tana.strftime("%d/%m/%Y")
print("Tere! \nTäna on",kys)

inger = tana.strftime("%B %d, %Y")
print("Tere! \nTäna on",inger)

zinger = tana.strftime("%m/%d/%y")
print("Tere! \nTäna on",zinger)

gsf = tana.strftime("%b-%d-%Y")
print("Tere! \nTäna on",gsf)

print("Täna on", tana.day)
print("päev, kuu number on", tana.month)
print("ja aasta on", tana.year)

month(theyear=2026,themonth=10)
nigger=monthrange(tana.year, tana.month)
print(nigger,"on jäänud kuu lõpuni")
aastalõpuni=(date(tana.year, 12, 31) - tana).days
print("Aasta lõpuni on jäänud", aastalõpuni, "päeva.")
sünnipäev=date(2009, 3, 25)
vanus=aastalõpuni//365
print("Oled",vanus,"aastat,", (aastalõpuni%365)//30, "kuud ja")
print((aastalõpuni%365)//30, "kuud ja")
print((aastalõpuni%365)%30 ,"päeva vana.")

# Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
# +Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
# +Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.

print("3 + 8 / (4 - 2) * 4 =", 3 + 8 / (4 - 2) * 4)
print("3 + 8 / 4 - 2 * 4 =", 3 + 8 / 4 - 2 * 4)
print("(3 + 8) / 4 - 2 * 4 =", (3 + 8) / 4 - 2 * 4)
try:
  R = float(input("R: "))
  print("Ruudu pindala:", R**2)
  print("Ruudu ümbermõõt:", 4*R)
  print("Ringi pindala:", pi*R**2)
  print("Ringi ümbermõõt:", 2*pi*R)
except ValueError:
    print("sisse number dumbass")

# Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes müntides ehk teisisõnu: kui palju 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa. Kasuta teadmist, et Maa raadius ekvaatori kohal on 6378 km.
# Algandmed (Maa raadius, mündi läbimõõt jne) omista programmi alguses sisukate nimedega muutujatele. Kuna ümbermõõdu arvutamiseks tuleb kasutada  PI-d (3,14...), siis võid selle (umbkaudse) väärtuse otse programmi kirjutada.  
# Püüdke välja mõelda viise, kuidas juhuslikest vigadest valemis hoiduda (teisendamised, ümardamise täpsus jne). Võimalusel võrrelge tulemusi teistega. Kui on erinevusi, leidke ühiselt põhjused.
# Kas programm on piisavalt hästi kirjutatud, et algandmete muutumise korral (näiteks juhul, kui on vaja arvutada Marsi ümbermõõtu 1-eurostes müntides) on parandusi selge ja lihtne teha?

earth_km = 6378

earth_perimeter_m = 2 * pi *(earth_km * 1000)

dmonetki = 0.02575

montki = earth_perimeter_m / dmonetki

print(f"dlina ekvatora: {earth_perimeter_m:,.2f} m")
print(f"2 euro: {montki:,.0f}")

a="Kill-koll"
b="Killadi-koll"
print(a.upper() * 3 + b.upper() + a.upper() * 3 + b.upper() + a.upper() * 3)

print("""Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.""".upper())

a = float(input("Sisesta esimese külje pikkus: "))
b = float(input("Sisesta teise külje pikkus: "))

U = 2 * (a + b)
S = a * b

print("Ümbermõõt:", U)
print("Pindala:", S)

kütus = float(input("Mitu liitrit kütust tangiti? "))
km = float(input("Mitu kilomeetrit läbiti? "))

kulu = kütus / km * 100

print("Keskmine kütusekulu:", round(kulu, 2), "l/100 km")

M = float(input("Mitu minutit rulluisutati? "))

kaugus = 29.9 * M / 60

print("Läbitud vahemaa:", round(kaugus, 2), "km")

aeg = int(input("Sisesta aeg minutites: "))

tunnid = aeg // 60
minutid = aeg % 60

print(f"{tunnid}:{minutid:02d}")