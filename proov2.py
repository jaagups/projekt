import easygui
from random import randint

def raha():
    nupud = ["jah", "ei"]
    vajutus = easygui.buttonbox("kas mängid?", choices = nupud)
    if vajutus == "jah":
        f = open("blackjack.txt")
        sinu_raha = f.readline()
        f.close()
        panus = easygui.integerbox("kui palju panustad?", upperbound = int(sinu_raha))

def sinu_kaardid():
    kaardid = ["A","A","A","A",10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,8,8,8,8,7,7,7,7,6,6,6,6,5,5,5,5,4,4,4,4,3,3,3,3,2,2,2,2]
    kaart1 = kaardid[randint(0,51)]
    kaardid.remove(kaart1)
    if kaart1 == "A":
        buttons = [1, 11]
        valik = easygui.buttonbox("kas valid ässa väärtuseks 1 või 11?(praegu on sul 0)", choices = buttons)
        if valik == "1":
            kaart1 = 1
        else:
            kaart1 = 11
         
    kaart2 = kaardid[randint(0,50)]
    kaardid3 = kaardid.remove(kaart2)
    kaardid.remove(kaart2)
    if kaart2 == "A":
        buttons = [1, 11]
        valik = easygui.buttonbox("kas valid ässa väärtuseks 1 või 11?(praegu on sul" + str(kaart1) + ")", choices = buttons)
        if valik == "1":
            kaart2 = 1
        else:
            kaart2 = 11
    summa1 = int(kaart1) + int(kaart2)
    if summa1 == 21:
        print("võitsid")
    else:
        nupud = ["jah", "ei"]
        valik = easygui.buttonbox("kas võtad kolmanda kaardi?(praegu on sul " + str(summa1) + ")", choices = nupud)
        if valik == "jah":
            kaart3 = kaardid[randint(0, 49)]
            if kaart3 == "A":
                buttons = [1, 11]
                valik = easygui.buttonbox("kas valid ässa väärtuseks 1 või 11?(praegu on sul " + str(summa1) + ")", choices = buttons)
                if valik == "1":
                    kaart3 = 1
                    summa2 = int(kaart1) + int(kaart2) + int(kaart3)
                    easygui.msgbox("s2 " + str(summa2))
                else:
                    kaart3 = 11
                    summa2 = int(kaart1) + int(kaart2) + int(kaart3)
                    easygui.msgbox("s2 " + str(summa2))
            else:
                summa2 = int(kaart1) + int(kaart2) + int(kaart3)
                easygui.msgbox("s2 " + str(summa2))
            if summa2 > 21:
                easygui.msgbox("putsis")
                return
        else:
            easygui.msgbox(summa1)


sinu_kaardid()