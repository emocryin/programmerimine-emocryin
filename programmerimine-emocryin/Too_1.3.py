from calendar import *
from datetime import *
from math import *

tana = date.today()
print("Tere! \nTäna on",tana)

# kys = tana.strftime("%d/%m/%Y")
# print("Tere! \nTäna on",kys)

# inger = tana.strftime("%B %d, %Y")
# print("Tere! \nTäna on",inger)

# zinger = tana.strftime("%m/%d/%y")
# print("Tere! \nTäna on",zinger)

# gsf = tana.strftime("%b-%d-%Y")
# print("Tere! \nTäna on",gsf)

# print("Täna on", tana.day)
# print("päev, kuu number on", tana.month)
# print("ja aasta on", tana.year)

# month(theyear=2026,themonth=10)
# nigger=monthrange(tana.year, tana.month)
# print(nigger,"on jäänud kuu lõpuni")
# aastalõpuni=(date(tana.year, 12, 31) - tana).days
# print("Aasta lõpuni on jäänud", aastalõpuni, "päeva.")
# sünnipäev=date(2009, 3, 25)
# vanus=aastalõpuni//365
# print("Oled",vanus,"aastat,", (aastalõpuni%365)//30, "kuud ja")
# print((aastalõpuni%365)//30, "kuud ja")
# print((aastalõpuni%365)%30 ,"päeva vana.")

# Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
# +Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
# +Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.

# print("3 + 8 / (4 - 2) * 4 =", 3 + 8 / (4 - 2) * 4)
# print("3 + 8 / 4 - 2 * 4 =", 3 + 8 / 4 - 2 * 4)
# print("(3 + 8) / 4 - 2 * 4 =", (3 + 8) / 4 - 2 * 4)
try:
  R = float(input("R: "))
  print("Ruudu pindala:", R**2)
  print("Ruudu ümbermõõt:", 4*R)
  print("Ringi pindala:", pi*R**2)
  print("Ringi ümbermõõt:", 2*pi*R)
except ValueError:
    print("sisse number dumbass")