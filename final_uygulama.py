from tkinter import*
import tkinter
import random

pencere=tkinter.Tk()
frame=tkinter.Frame(pencere,background="black",width="500",height="500")
etiket=pencere.title("Simon Oyunu")

level=tkinter.Label(pencere,background="grey",fg="white",text="Level:",font="times 10 bold")
level.place(x=20, y=20)

l=0

levelno=tkinter.Label(pencere,background="grey",fg="white",text=l,font="times 10 bold")
levelno.place(x=60,y=20)

liste=[]
renk=0

def sarıliste():
    sarı.configure(background="white")
    sarı.after(500,lambda: sarı.configure(background="yellow"))
    global liste
    global renk
    renk=1
    liste.append(renk)
sarı=tkinter.Button(pencere, bd="0",width="20",height="10",background="yellow",command=sarıliste)
sarı.place(x=50,y=50)

def maviliste():
    mavi.configure(background="white")
    mavi.after(500,lambda: mavi.configure(background="blue"))
    global liste
    global renk
    renk=2
    liste.append(renk)
mavi=tkinter.Button(pencere,bd="0",width="20",height="10", background="blue",command=maviliste)
mavi.place(x=300,y=50)

def kırmızıliste():
    kırmızı.configure(background="white")
    kırmızı.after(500,lambda: kırmızı.configure(background="red"))
    global liste
    global renk
    renk=3
    liste.append(renk)
kırmızı=tkinter.Button(pencere,bd="0",width="20",height="10", background="red",command=kırmızıliste)
kırmızı.place(x=50,y=260)

def yeşilliste():
    yeşil.configure(background="white")
    yeşil.after(500,lambda: yeşil.configure(background="green"))
    global liste
    global renk
    renk=4
    liste.append(renk)
yeşil=tkinter.Button(pencere,bd="0",width="20",height="10",background="green",command=yeşilliste)
yeşil.place(x=300,y=260)

def levelup():
    global l
    l=l+1
    levelno.configure(text=l)

r=random.randint(1,4)
sıra=[]

def sırakontrol():
    global liste
    global sıra
    if liste==sıra:
        levelup()

def sıragoster():
    global r
    global sıra

    if r==1:
        sarı.configure(background="white")
        sarı.after(500, lambda: sarı.configure(background="yellow"))
        sıra.append(r)
        pencere.after(2000,sırakontrol)

    elif r==2:
        mavi.configure(background="white")
        mavi.after(500, lambda: mavi.configure(background="blue"))
        sıra.append(r)
        pencere.after(2000,sırakontrol)

    elif r==3:
        kırmızı.configure(background="white")
        kırmızı.after(500, lambda: kırmızı.configure(background="red"))
        sıra.append(r)
        pencere.after(2000,sırakontrol)

    elif r==4:
        yeşil.configure(background="white")
        yeşil.after(500, lambda: yeşil.configure(background="green"))
        sıra.append(r)
        pencere.after(2000,sırakontrol)

pencere.after(800,sıragoster)

frame.pack()
pencere.resizable(False,False)
pencere.mainloop()






