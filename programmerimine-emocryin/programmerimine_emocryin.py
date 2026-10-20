from xml.sax.xmlreader import IncrementalParser
import math


print("Tere tulemast! Üks hetk, palun...")
print("Esimine programm, mis on kirjutatud Pythonis.")
#muutujad
kursus=2

print("Ma õpin",1,"kuursusel") #sep=" ", end="\n"
print("Ma õpin",kursus,".kuursusel",sep="***",end=". ")
kursus=int(input("Aga sina? "))
print("Tore! Sa õpib",kursus,".kursusel. Aga järgmisel aastal",kursus+1,"kursusel.")

nimi = input("Mis su nimi on? ")
print(nimi,"õpib ",kursus,". kursusel")

a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a * b)

a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a + b)

a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a - b)

a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a / b)

a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a // b)

a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a % b)

a =float(input("Esimene arv: "))
b =float(input("Teine arv: "))
print(a ** b)

a = int(input("Esimene arv: "))
b = int(input("Teine arv: "))
print(a,"+",b,"=",a + b) #liitmine
print(a,"-",b,"=",a - b) #lahutamine
print(a,"*",b,"=",a * b) #korrutamine
print(a,"/",b,"=",a / b) #jagamine
print(a,"//",b,"=",a // b) #jagamise täisarvuline osa
print(a,"%",b,"=",a % b) #jagamisjääk
print(a,"**",b,"=",a ** b) #astendamine

#f-sõne kasutamine
nimi = "Mari"
punktid = 87
print(f"{nimi} sai {punktid} punkti.")
hind = 19.9
kogus = 3
print(f"Kokku: {hind * kogus:.2f} eurot")

#stringide ühendamine ja korrutamine
print("Tere" + " " + "päevast")
print("-" * 20)
vanus = 17
print("Vanus: " + str(vanus))

#math mooduli kasutamine
print("Pii väärtus:", math.pi)
print("√16 =", math.sqrt(16))
print("sin(π/2) =", math.sin(math.pi / 2))
print("sin(30°) =", round(math.sin(math.radians(30)), 2))
print("5! =", math.factorial(5))

