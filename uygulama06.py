from tkinter import Tk, Label, Button, LEFT, RIGHT,font
import random
class sozler:
    def __init__(self, master):
        self.master = master
        master.title("Günün sözleri")

        self.baslık = Label(master, text="Günün Sözü" , font="times 20 bold" , bg="yellow" )
        self.baslık.pack()

        self.tıkla = Button(master, text="Tıkla",command=self.sozyazdır  , font="times 13" , bg="grey")
        self.tıkla.pack()
        self.tıkla.pack(side=LEFT)

        self.kapat = Button(master, text="Kapat", command=master.quit, font="times 13" , bg="grey" )
        self.kapat.pack()
        self.kapat.pack(side=RIGHT)

    def sozyazdır(self):
        sozler=["Başkalarının yanlışlarından öğrenmeliyiz.Hepsini kendimiz yapacak kadar zamanımız yok.","İnancını asla yitirme.","Kendine inan.","Pes ediyorum! dediğiniz anda aynı durumla karşılaşan başka birinin hey! ne büyük fırsat dediğini unutmayın.","Yapamazsın diyenler yapanları durduramadı.","Yaşayan, yaşamayan her varlıkta güzelliği ara."]
        secilensozler=random.choice(sozler)
        self.soz=Label(self.master, text=secilensozler)
        self.soz.pack()

root = Tk()
secilensoz = sozler(root)
root.mainloop()

