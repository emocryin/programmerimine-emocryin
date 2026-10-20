from math import *
import random
from tkinter import ROUND

# Kirjuta enda esimene programm, mis väljastab käsureale teksti: 
#  “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: 
#  “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”
# Ülesanne 1
# print("Tere, maailm!")
# nimi = input("Mis su nimi on? ")
# print("Tere, maailm! Tervitan sind",nimi)
# try:
#     vanus = int(input("Kui vana sa oled? "))
#     print("Tere, maailm! Tervitan sind",nimi,"! Sa oled",vanus,"aastat vana.")
# except ValueError:
#     print("Palun sisesta oma vanus numbrina.")
# # Mis tüüpi on järgnevad muutujad:
# Ülesanne 2
# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 16.5
# d) kas_käib_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# Kirjuta kood tüüpide kontrollimiseks.

# vanus = 18
# eesnimi = "Jaak"
# pikkus = 16.5
# kas_käib_koolis = True
# print("vanus", vanus, "tüüp:", type(vanus))
# print("eesnimi", eesnimi, "tüüp:", type(eesnimi))
# print("pikkus", pikkus, "tüüp:", type(pikkus))
# print("kas_käib_koolis", kas_käib_koolis, "tüüp:", type(kas_käib_koolis))

# # В вашем коде запишите количество конфет на столе в переменную (количество конфет случайное). Затем отобразите количество конфет в переменной на экране с помощью команды print().
# # Запросите у пользователя, сколько конфет он хочет убрать со стола. Удалите желаемое количество конфет из количества конфет на столе и отобразите количество конфет на экране.

kommid = random.randint(15, 50)
print("Laual on", kommid,"kommid")
try:
   kommid_tahad = int(input("Kui palju tahad kommid? "))
   kommid -=kommid_tahad
   print("Laual on nüüd", kommid, "kommi.")
except ValueError:
   print("Palun sisesta oma kommid numbrina.")

# # Puu läbimõõdu arvutamine
# # Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.
# ümbermõõt=float(input("Sisesta puu ümbermõõt: "))

# läbimõõt=ümbermõõt/pi
# print("Puu läbimõõt on:", läbimõõt)

# # Ülesanne 5
# # Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
# N = float(input("Sisesta maatüki pikkus (N): "))
# M = float(input("Sisesta maatüki laius (M): "))
# diagonaal = sqrt(N**2 + M**2)
# print("Ristkülikukujulise maatüki diagonaal on:", round(diagonaal,2))

# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = teepikkus / aeg

# print("Sinu kiirus oli " + str(kiirus) + " km/h")

# n1 = int(input("Arv 1: "))
# n2 = int(input("Arv 2: "))
# n3 = int(input("Arv 3: "))
# n4 = int(input("Arv 4: "))
# n5 = int(input("Arv 5: "))

# summa = n1 + n2 + n3 + n4 + n5
# jägaja=int(input("Sisesta arv, millega jagada: "))
# keskmine = summa / 5
# print("Aritmeetilise keskmise on: ",keskmine)
# print("Täisarvuline osa:", int(keskmine))
# print("Jääk:", summa % jägaja)

# print(" @..@")
# print("(----)")
# print("(\__/)")
# print("^^  ^^")

# # a = int(input("Sisesta külje a: "))
# # b = int(input("Sisesta külje b: "))
# # c = int(input("Sisesta külje c: "))

# # P = a + b + c

# # print("Ümbermõõt on:",P)

# sõbrad = random.randint(1, 4)
# pitsa_hind = 12.90
# jootraha = pitsa_hind * 0.10
# kogusumma = pitsa_hind + jootraha

# maksab_igaüks = kogusumma / sõbrad

# print("Kogusumma koos jootrahaga:", round(kogusumma, 2),"euro")
# print("Igaüks peab maksma:", round(maksab_igaüks, 2),"euro")