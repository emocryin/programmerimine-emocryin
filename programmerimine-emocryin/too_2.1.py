#1. Juku
#a) Programm küsib eesnime. Kui nimi on Juku, kuvatakse „Lähme Jukuga kinno!“, muidu teatatakse, et täna kinno ei minda.
#Programm peab Juku ära tundma ka siis, kui nimi on kirjutatud suurtähtedega (JUKU) või väiketähtedega (juku).
#Kui nimi on kirjutatud ainult suurtähtedega, lisa märkus „Ära karju, Juku!“.
#Kasuta: lower(), isupper()

eesnimi=input("Sisesta eesnimi: ")
if eesnimi.lower() == "juku":
    print("Lähme Jukuga kinno!")
    if eesnimi.isupper():
        print("Ära karju, Juku!")
    elif eesnimi.islower():
        print("Ära sosista, Juku!")
    #Kui kinno läheb Juku, küsi tema vanus ja otsusta, millist piletit on vaja osta
    vanus=input(f"Kui vana on {eesnimi}?")
    if vanus.isdigit():
        vanus=int(vanus)
        if   0<vanus<6:
            pilet="Tasuta pilet"
        elif 6<=vanus<=14:
            pilet="Lapsepilet"
        elif 14<=vanus<65:
            pilet="Täispilet"
        elif 65<=vanus<=100:
            pilet="Sooduspilet"
        else:
            pilet="Tundmatu pilet"
            print(f"{eesnimi} vajab {pilet}.")
    else:
        print("Viga andmedega")
else:
    print("Täna kinno ei minda.")
#Kui kinno läheb Juku, küsi tema vanus ja otsusta, millist piletit on vaja osta

#Küsi kahe inimese nimed. Kontrolli, kas mõlemad nimed koosnevad ainult tähtedest. Kui jah, teata kasutajale, 
#kas nad on täna pinginaabrid või mitte. Kui mõnes nimes on numbreid või muid märke, kuva veateade.
#Otsusta ise, kuidas „pinginaabrid“ määratakse, näiteks juhuslikult või nimede algustähtede järgi.

pinginaabrid=["Romanich","Kiruha"]
nimi1=input("Sisesta nimi: ")