from tkinter import *
import time
import winsound
import datetime

def alarm(zvn, zvn2, zvn3, zvn4, zvn5, zvn6, zvn7, zvn8, zvn1, zvn12, zvn13, zvn14, zvn15, zvn16, zvn17, zvn18, zvn21, zvn22, zvn23, zvn24, zvn25, zvn26, zvn27, zvn28, zvn31, zvn32, zvn33, zvn34, zvn35, zvn36, zvn37, zvn38):
    while True:
        time.sleep(20)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M")
        print(now)

        if now == zvn:
            print("ЗВОНОК с 1")
            winsound.PlaySound("1.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn2:
            print("ЗВОНОК с 2")
            winsound.PlaySound("2.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn3:
            print("ЗВОНОК с 3")
            winsound.PlaySound("3.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn4:
            print("ЗВОНОК с 4")
            winsound.PlaySound("4.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn5:
            print("ЗВОНОК с 5")
            winsound.PlaySound("5.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn6:
            print("ЗВОНОК с 6")
            winsound.PlaySound("6.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn7:
            print("ЗВОНОК с 7")
            winsound.PlaySound("7.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn8:
            print("ЗВОНОК с 8")
            winsound.PlaySound("8.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn1:
            print("ЗВОНОК на 1")
            winsound.PlaySound("9.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn12:
            print("ЗВОНОК на 2")
            winsound.PlaySound("10.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn13:
            print("ЗВОНОК на 3")
            winsound.PlaySound("11.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn14:
            print("ЗВОНОК на 4")
            winsound.PlaySound("12.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn15:
            print("ЗВОНОК на 5")
            winsound.PlaySound("13.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn16:
            print("ЗВОНОК на 6")
            winsound.PlaySound("14.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn17:
            print("ЗВОНОК на 7")
            winsound.PlaySound("15.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn18:
            print("ЗВОНОК на 8")
            winsound.PlaySound("16.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn21:
            print("ЗВОНОК на 1")
            winsound.PlaySound("17.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn22:
            print("ЗВОНОК на2")
            winsound.PlaySound("18.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn23:
           print("ЗВОНОК на3")
           winsound.PlaySound("19.wav", winsound.SND_ASYNC)
           time.sleep(180)
        if now == zvn24:
            print("ЗВОНОК на4")
            winsound.PlaySound("20.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn25:
            print("ЗВОНОК на5")
            winsound.PlaySound("21.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn26:
            print("ЗВОНОК на6")
            winsound.PlaySound("22.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn27:
            print("ЗВОНОК на7")
            winsound.PlaySound("23.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn28:
            print("ЗВОНОК на8")
            winsound.PlaySound("24.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn31:
            print("ЗВОНОК c 1")
            winsound.PlaySound("25.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn32:
            print("ЗВОНОК cо 2")
            winsound.PlaySound("26.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn33:
           print("ЗВОНОК с 3")
           winsound.PlaySound("27.wav", winsound.SND_ASYNC)
           time.sleep(180)
        if now == zvn34:
            print("ЗВОНОК с 4")
            winsound.PlaySound("28.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn35:
            print("ЗВОНОК с 5")
            winsound.PlaySound("29.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn36:
            print("ЗВОНОК с 6")
            winsound.PlaySound("30.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn37:
            print("ЗВОНОК с 7")
            winsound.PlaySound("31.wav", winsound.SND_ASYNC)
            time.sleep(180)
        if now == zvn38:
            print("ЗВОНОК с 8")
            winsound.PlaySound("32.wav", winsound.SND_ASYNC)
            time.sleep(180)

def actual_time():
    zvn = f"{hour1.get()}:{min1.get()}"
    zvn2 = f"{hour2.get()}:{min2.get()}"
    zvn3 = f"{hour3.get()}:{min3.get()}"
    zvn4 = f"{hour4.get()}:{min4.get()}"
    zvn5 = f"{hour5.get()}:{min5.get()}"
    zvn6 = f"{hour6.get()}:{min6.get()}"
    zvn7 = f"{hour7.get()}:{min7.get()}"
    zvn8 = f"{hour8.get()}:{min8.get()}"
    zvn1 = f"{hour11.get()}:{min11.get()}"
    zvn12 = f"{hour12.get()}:{min12.get()}"
    zvn13 = f"{hour13.get()}:{min13.get()}"
    zvn14 = f"{hour14.get()}:{min14.get()}"
    zvn15 = f"{hour15.get()}:{min15.get()}"
    zvn16 = f"{hour16.get()}:{min16.get()}"
    zvn17 = f"{hour17.get()}:{min17.get()}"
    zvn18 = f"{hour18.get()}:{min18.get()}"
    zvn21 = f"{hour21.get()}:{min21.get()}"
    zvn22 = f"{hour22.get()}:{min22.get()}"
    zvn23 = f"{hour23.get()}:{min23.get()}"
    zvn24 = f"{hour24.get()}:{min24.get()}"
    zvn25 = f"{hour25.get()}:{min25.get()}"
    zvn26 = f"{hour26.get()}:{min26.get()}"
    zvn27 = f"{hour27.get()}:{min27.get()}"
    zvn28 = f"{hour28.get()}:{min28.get()}"
    zvn31 = f"{hour31.get()}:{min31.get()}"
    zvn32 = f"{hour32.get()}:{min32.get()}"
    zvn33 = f"{hour33.get()}:{min33.get()}"
    zvn34 = f"{hour34.get()}:{min34.get()}"
    zvn35 = f"{hour35.get()}:{min35.get()}"
    zvn36 = f"{hour36.get()}:{min36.get()}"
    zvn37 = f"{hour37.get()}:{min37.get()}"
    zvn38 = f"{hour38.get()}:{min38.get()}"
    alarm(zvn, zvn2, zvn3, zvn4, zvn5, zvn6, zvn7, zvn8, zvn1, zvn12, zvn13, zvn14, zvn15, zvn16, zvn17, zvn18, zvn21, zvn22, zvn23, zvn24, zvn25, zvn26, zvn27, zvn28, zvn31, zvn32, zvn33, zvn34, zvn35, zvn36, zvn37, zvn38)



clock = Tk()     # замена
clock.title("ZVONOK BY DIMA 10Б")             # тайтл

clock.geometry("590x300")
nowy= time.strftime
TXTwithTIME = Label(clock, text = "начало урока", font=("Arial",8,"bold")).place(x = 35)
TXTwithTIME2 = Label(clock, text = "конец урока", font=("Arial",8,"bold")).place(x = 210)
TXTwithSMENE1 = Label(clock, text = "1 смена", font=1).place(x = 125)
TXTwithSMENE2 = Label(clock, text = "2 смена", font=1).place(x = 385)
TXTwithTIME3 = Label(clock, text = "начало урока", font=("Arial",8,"bold")).place(x = 295)
TXTwithTIME4 = Label(clock, text = "конец урока", font=("Arial",8,"bold")).place(x = 470)
TXTwithNAME = Label(clock, text = "CREATED BY DIMA 10Б", font=("Lucida Console",9,"bold")).place( y=280)
TXT1LESN = Label(clock, text = "1 урок",fg="black",relief = "solid", font=("Helevetica",7,"bold")).place(x=0, y=30)
TXT2LESN = Label(clock, text = "2 урок",fg="black",relief = "solid", font=("Helevetica",7,"bold")).place(x=0, y=60)
TXT3LESN = Label(clock, text = "3 урок",fg="black",relief = "solid", font=("Helevetica",7,"bold")).place(x=0, y=90)
TXT4LESN = Label(clock, text = "4 урок",fg="black",relief = "solid", font=("Helevetica",7,"bold")).place(x=0, y=120)
TXT5LESN = Label(clock, text = "5 урок",fg="black",relief = "solid", font=("Helevetica",7,"bold")).place(x=0, y=150)
TXT6LESN = Label(clock, text = "6 урок",fg="black",relief = "solid", font=("Helevetica",7,"bold")).place(x=0, y=180)
TXT7LESN = Label(clock, text = "7 урок",fg="black",relief = "solid", font=("Helevetica",7,"bold")).place(x=0, y=210)
TXT8LESN = Label(clock, text = "8 урок",fg="black",relief = "solid", font=("Helevetica",7,"bold")).place(x=0, y=240)
TXT11LESN = Label(clock, text = "1 урок",fg="black",relief = "solid", font=("Helevetica",7,"bold")).place(x=550, y=30)
TXT12LESN = Label(clock, text = "2 урок",fg="black",relief = "solid", font=("Helevetica",7,"bold")).place(x=550, y=60)
TXT13LESN = Label(clock, text = "3 урок",fg="black",relief = "solid", font=("Helevetica",7,"bold")).place(x=550, y=90)
TXT14LESN = Label(clock, text = "4 урок",fg="black",relief = "solid", font=("Helevetica",7,"bold")).place(x=550, y=120)
TXT15LESN = Label(clock, text = "5 урок",fg="black",relief = "solid", font=("Helevetica",7,"bold")).place(x=550, y=150)
TXT16LESN = Label(clock, text = "6 урок",fg="black",relief = "solid", font=("Helevetica",7,"bold")).place(x=550, y=180)
TXT17LESN = Label(clock, text = "7 урок",fg="black",relief = "solid", font=("Helevetica",7,"bold")).place(x=550, y=210)
TXT18LESN = Label(clock, text = "8 урок",fg="black",relief = "solid", font=("Helevetica",7,"bold")).place(x=550, y=240)

hour1 = StringVar()
min1 = StringVar()
hourTime= Entry(clock,textvariable = hour1,bg = "white",width = 5).place(x=40,y=30)
minTime= Entry(clock,textvariable = min1,bg = "white",width = 5).place(x=80,y=30)


hour2 = StringVar()
min2 = StringVar()
hourTime2= Entry(clock,textvariable = hour2,bg = "white",width = 5).place(x=40,y=60)
minTime2= Entry(clock,textvariable = min2,bg = "white",width = 5).place(x=80,y=60)



hour3 = StringVar()
min3 = StringVar()
hourTime3= Entry(clock,textvariable = hour3,bg = "white",width = 5).place(x=40,y=90)
minTime3= Entry(clock,textvariable = min3,bg = "white",width = 5).place(x=80,y=90)


hour4 = StringVar()
min4 = StringVar()
hourTime4= Entry(clock,textvariable = hour4,bg = "white",width = 5).place(x=40,y=120)
minTime4= Entry(clock,textvariable = min4,bg = "white",width = 5).place(x=80,y=120)


hour5 = StringVar()
min5 = StringVar()
hourTime5= Entry(clock,textvariable = hour5,bg = "white",width = 5).place(x=40,y=150)
minTime5= Entry(clock,textvariable = min5,bg = "white",width = 5).place(x=80,y=150)


hour6 = StringVar()
min6 = StringVar()
hourTime6= Entry(clock,textvariable = hour6,bg = "white",width = 5).place(x=40,y=180)
minTime6= Entry(clock,textvariable = min6,bg = "white",width = 5).place(x=80,y=180)


hour7 = StringVar()
min7 = StringVar()
hourTime7= Entry(clock,textvariable = hour7,bg = "white",width = 5).place(x=40,y=210)
minTime7= Entry(clock,textvariable = min7,bg = "white",width = 5).place(x=80,y=210)


hour8 = StringVar()
min8 = StringVar()
hourTime8= Entry(clock,textvariable = hour8,bg = "white",width = 5).place(x=40,y=240)
minTime8= Entry(clock,textvariable = min8,bg = "white",width = 5).place(x=80,y=240)


hour11 = StringVar()
min11 = StringVar()
hourTime11= Entry(clock,textvariable = hour11,bg = "white",width = 5).place(x=210,y=30)
minTime11= Entry(clock,textvariable = min11,bg = "white",width = 5).place(x=250,y=30)


hour12 = StringVar()
min12 = StringVar()
hourTime12= Entry(clock,textvariable = hour12,bg = "white",width = 5).place(x=210,y=60)
minTime12= Entry(clock,textvariable = min12,bg = "white",width = 5).place(x=250,y=60)



hour13 = StringVar()
min13 = StringVar()
hourTime13= Entry(clock,textvariable = hour13,bg = "white",width = 5).place(x=210,y=90)
minTime13= Entry(clock,textvariable = min13,bg = "white",width = 5).place(x=250,y=90)


hour14 = StringVar()
min14 = StringVar()
hourTime14= Entry(clock,textvariable = hour14,bg = "white",width = 5).place(x=210,y=120)
minTime14= Entry(clock,textvariable = min14,bg = "white",width = 5).place(x=250,y=120)


hour15 = StringVar()
min15 = StringVar()
hourTime15= Entry(clock,textvariable = hour15,bg = "white",width = 5).place(x=210,y=150)
minTime15= Entry(clock,textvariable = min15,bg = "white",width = 5).place(x=250,y=150)


hour16 = StringVar()
min16 = StringVar()
hourTime16= Entry(clock,textvariable = hour16,bg = "white",width = 5).place(x=210,y=180)
minTime16= Entry(clock,textvariable = min16,bg = "white",width = 5).place(x=250,y=180)


hour17 = StringVar()
min17 = StringVar()
hourTime17= Entry(clock,textvariable = hour17,bg = "white",width = 5).place(x=210,y=210)
minTime17= Entry(clock,textvariable = min17,bg = "white",width = 5).place(x=250,y=210)


hour18 = StringVar()
min18 = StringVar()
hourTime18= Entry(clock,textvariable = hour18,bg = "white",width = 5).place(x=210,y=240)
minTime18= Entry(clock,textvariable = min18,bg = "white",width = 5).place(x=250,y=240)


hour21 = StringVar()
min21 = StringVar()
hourTime21= Entry(clock,textvariable = hour21,bg = "white",width = 5).place(x=300,y=30)
minTime21= Entry(clock,textvariable = min21,bg = "white",width = 5).place(x=340,y=30)


hour22 = StringVar()
min22 = StringVar()
hourTime22= Entry(clock,textvariable = hour22,bg = "white",width = 5).place(x=300,y=60)
minTime22= Entry(clock,textvariable = min22,bg = "white",width = 5).place(x=340,y=60)



hour23 = StringVar()
min23 = StringVar()
hourTime23= Entry(clock,textvariable = hour23,bg = "white",width = 5).place(x=300,y=90)
minTime23= Entry(clock,textvariable = min23,bg = "white",width = 5).place(x=340,y=90)


hour24 = StringVar()
min24 = StringVar()
hourTime24= Entry(clock,textvariable = hour24,bg = "white",width = 5).place(x=300,y=120)
minTime24= Entry(clock,textvariable = min24,bg = "white",width = 5).place(x=340,y=120)


hour25 = StringVar()
min25 = StringVar()
hourTime25= Entry(clock,textvariable = hour25,bg = "white",width = 5).place(x=300,y=150)
minTime25= Entry(clock,textvariable = min25,bg = "white",width = 5).place(x=340,y=150)


hour26 = StringVar()
min26 = StringVar()
hourTime26= Entry(clock,textvariable = hour26,bg = "white",width = 5).place(x=300,y=180)
minTime26= Entry(clock,textvariable = min26,bg = "white",width = 5).place(x=340,y=180)


hour27 = StringVar()
min27 = StringVar()
hourTime27= Entry(clock,textvariable = hour27,bg = "white",width = 5).place(x=300,y=210)
minTime27= Entry(clock,textvariable = min27,bg = "white",width = 5).place(x=340,y=210)


hour28 = StringVar()
min28 = StringVar()
hourTime28= Entry(clock,textvariable = hour28,bg = "white",width = 5).place(x=300,y=240)
minTime28= Entry(clock,textvariable = min28,bg = "white",width = 5).place(x=340,y=240)

hour31 = StringVar()
min31 = StringVar()
hourTime31= Entry(clock,textvariable = hour31,bg = "white",width = 5).place(x=470,y=30)
minTime31= Entry(clock,textvariable = min31,bg = "white",width = 5).place(x=510,y=30)


hour32 = StringVar()
min32 = StringVar()
hourTime32= Entry(clock,textvariable = hour32,bg = "white",width = 5).place(x=470,y=60)
minTime32= Entry(clock,textvariable = min32,bg = "white",width = 5).place(x=510,y=60)



hour33 = StringVar()
min33 = StringVar()
hourTime33= Entry(clock,textvariable = hour33,bg = "white",width = 5).place(x=470,y=90)
minTime33= Entry(clock,textvariable = min33,bg = "white",width = 5).place(x=510,y=90)


hour34 = StringVar()
min34 = StringVar()
hourTime34= Entry(clock,textvariable = hour34,bg = "white",width = 5).place(x=470,y=120)
minTime34= Entry(clock,textvariable = min34,bg = "white",width = 5).place(x=510,y=120)


hour35 = StringVar()
min35 = StringVar()
hourTime35= Entry(clock,textvariable = hour35,bg = "white",width = 5).place(x=470,y=150)
minTime35= Entry(clock,textvariable = min35,bg = "white",width = 5).place(x=510,y=150)


hour36 = StringVar()
min36 = StringVar()
hourTime36= Entry(clock,textvariable = hour36,bg = "white",width = 5).place(x=470,y=180)
minTime36= Entry(clock,textvariable = min36,bg = "white",width = 5).place(x=510,y=180)


hour37 = StringVar()
min37 = StringVar()
hourTime37= Entry(clock,textvariable = hour37,bg = "white",width = 5).place(x=470,y=210)
minTime37= Entry(clock,textvariable = min37,bg = "white",width = 5).place(x=510,y=210)


hour38 = StringVar()
min38 = StringVar()
hourTime38= Entry(clock,textvariable = hour38,bg = "white",width = 5).place(x=470,y=240)
minTime38= Entry(clock,textvariable = min38,bg = "white",width = 5).place(x=510,y=240)




submit = Button(clock,text = "СОХРАНИТЬ",fg="black",bg="magenta",width = 10,command = actual_time).place(x =252,y=270)
clock.mainloop()


