#lihtne if lause

# try:
#    x = int(input("Sisesta arv: "))
#    if x > 0:
#     print("Positiivne arv")
#     print("See rida on ka if-i sees")
#    print("See rida täidetakse alati")
# except ValueError:
#     print("Valed andmed")

#if... else lause
# try:

#    vanus = int(input("Kui vana sa oled?: "))
#    if vanus > 18:
#     print("Saab valida")
#    else: 
#     print("go away fucking scumbag")
# except ValueError:
#     print("muhahahah")
# try:
#    x = int(input("Sisesta arv: "))
#    if x == 1:
#     print("Õige")
#    else: 
#     print("Vale")
# except ValueError:
#     print("Not number, dumbass!") 

# #if...elif...else
# try:
#    vanus = int(input("Sisesta vanus:"))
#    if vanus > 18:
#        print("Saab veebi sisse!")
#    elif 17 <= vanus <= 70:
#      print("123123")
#    else:
#        print("Ei saa!") 
# except ValueError:
#     print("Not number, dumbass!")
#2.5 if lause sees if lause
try: 
    nimi = input("Sisesta nimi: ")
    if nimi.isalpha():
        print("Nimi sobib.")
        vanus = int(input("Vanus: "))
        if vanus >= 18:
            juhiluba = input("Kas sul on juhiluba? (jah/ei) ")
            if juhiluba.lower() == "jah":
                print("Võid autot juhtida.")
            else:
                print("Kõigepealt tee juhiload.")
        else:
            print("Oled autojuhtimiseks liiga noor.")
    else:
       print("Nimes tohib olla ainult tähti!")

except ValueError:
    print("Not number, dumbass!")

