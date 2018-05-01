#!/usr/bin/env python
#-*-coding:utf-8-*-
from tkinter import *
import tkinter.messagebox
from tkinter import E,Y
from PIL import ImageTk,Image
class Katalogum:
    def __init__(self,anasayfa):
        self.anasayfa = anasayfa
        anasayfa.title("Kütüphane Otomasyonu")
        anasayfa.wm_iconbitmap("turk.ico")
        anasayfa.configure(background="black")

        self.foto = Image.open("foto.jpg")
        self.tkimage = ImageTk.PhotoImage(self.foto)
        self.resim = Label(root, image=self.tkimage)
        self.resim.grid()

        self.kitapları_listele = Button(anasayfa, text="Kitapları Listele",bg="black",fg="yellow",cursor="star",font="bold", command=self.kitaplari_listele)
        self.kitapları_listele.grid(row="1")

        self.kitap_ekle = Button(anasayfa, text="Kitap Ekle", bg="black",fg="yellow",cursor="star",font="bold",command = self.kitap_ekle)
        self.kitap_ekle.grid(row="2")

        self.kitap_sil = Button(anasayfa, text="Kitap Sil", bg="black",fg="yellow",cursor="star",font="bold",command=self.kitap_sil)
        self.kitap_sil.grid(row="3")

        self.kitap_günc = Button(anasayfa, text="Kitap Güncelle", bg="black",fg="yellow",cursor="star",font="bold",command=self.kitap_güncelle)
        self.kitap_günc.grid(row="4")

        self.kitap_ara = Button(anasayfa, text="Kitap Ara", bg="black",fg="yellow",cursor="star",font="bold",command=self.kitap_ara)
        self.kitap_ara.grid(row="5")

        Button(text="Hakkında", bg = "black", fg="Yellow", width=6, height=1, command=self.hakkinda).grid(row=6)

        self.cikis = Button(anasayfa, text ="Kapat", command=exit, fg="black", bg="yellow",cursor="man")
        self.cikis.grid(row="7")


    def kitap_ekle(self):
        global kitap_adi,yazar_adi,tur,isbn,yayinevi,yy,pencere1
        pencere1 = Tk()
        pencere1.wm_iconbitmap("turk.ico")
        baslik1 = pencere1.title("Kitap Kayıt Penceresi")
        pencere1.configure(background="black")

        kitap_adi= Entry(pencere1,width=27)
        kitap_adi.grid(column=2, row=3)
        yazar_adi = Entry(pencere1, width=27)
        yazar_adi.grid(column=2, row=4)
        tur = Entry(pencere1, width=27)
        tur.grid(column=2, row=5)
        isbn = Entry(pencere1, width=27)
        isbn.grid(column=2, row=6)
        yayinevi = Entry(pencere1, width=27)
        yayinevi.grid(column=2, row=7)
        yy = Entry(pencere1, width=27)
        yy.grid(column=2, row=8)
        self.kaydet = Button(pencere1, text= "Kaydet",command=self.kitap_kaydet, fg="black", bg="yellow")
        self.kaydet.grid(column=1, row=9)

        self.cıkıs = Button(pencere1 ,text = "Kapat", command=pencere1.destroy, fg="black", bg="yellow",cursor="man")
        self.cıkıs.grid(column=3, row=9)
        Label(pencere1,bg="black",fg="yellow", text='*********** ').grid(column=1, row=1)
        Label(pencere1,bg="black",fg="yellow", text='Kitap Adı: ').grid(column=1, row=3)
        Label(pencere1,bg="black",fg="yellow", text='Yazar Adı: ').grid(column=1, row=4)
        Label(pencere1,bg="black",fg="yellow", text='Kitabın Türü: ').grid(column=1, row=5)
        Label(pencere1,bg="black",fg="yellow", text='ISBN :').grid(column=1, row=6)
        Label(pencere1,bg="black",fg="yellow", text='Yayınevi : ').grid(column=1, row=7)
        Label(pencere1,bg="black",fg="yellow", text='Yayın Yılı :').grid(column=1, row=8)
    def kitap_kaydet(self):
        kayit_sis = str((kitap_adi.get() + "#" + yazar_adi.get() + "#" + tur.get() + "#" + isbn.get() + "#" + yayinevi.get() + "#" + yy.get())+"\n")
        dosya= open("katalog.txt","a")
        for i in kayit_sis:
            dosya.write(i)
        dosya.close()
        tkinter.messagebox.showinfo('Mesaj', 'Kitap Başarıyla Eklendi..')
        command=pencere1.destroy()

    def kitaplari_listele(self):
        pencerex= Tk()
        pencerex.wm_iconbitmap("turk.ico")
        baslik2 = pencerex.title("Kayıtlı Kitaplar")
        pencerex.configure(background="black")

        self.scroll = Scrollbar(pencerex)
        self.scroll.pack(side=RIGHT, fill=Y)
        file = open("katalog.txt")
        data = file.read()
        file.close()

        kitap_liste = Label(pencerex, text=data,fg="yellow", bg="black")
        kitap_liste.pack()

        self.cıkıs = Button(pencerex ,text = "Kapat", command=pencerex.destroy, fg="black", bg="yellow",cursor="man")
        self.cıkıs.pack()

    def kitap_sil(self):
        pencere2 = Tk()
        pencere2.wm_iconbitmap("turk.ico")
        baslik2 = pencere2.title("Kitap Silme Penceresi")
        pencere2.configure(background="black")
        tkinter.messagebox.showinfo('Mesaj', 'Kitap Silme Butonu Halihazırda Mevcut Değildir..\nÇok Yakında Kullanıma Sunulacaktır..')
        command=pencere2.destroy()


    def kitap_güncelle(self):
        pencere3 = Tk()
        pencere3.wm_iconbitmap("turk.ico")
        baslik3 = pencere3.title("Kitap Güncelleme Penceresi")
        pencere3.configure(background="black")
        tkinter.messagebox.showinfo('Mesaj','Kitap Güncelleme Butonu Halihazırda Mevcut Değildir..\nÇok Yakında Kullanıma Sunulacaktır..')
        command=pencere3.destroy()


    def kitap_ara(self):
        pencere4 = Tk()
        baslık4 = pencere4.title("Kitap arama penceresi")
        pencere4.configure(background="black")

        def kitap():
            pencerez = Tk()
            pencerez.wm_iconbitmap("turk.ico")
            baslik2 = pencerez.title("Aranılan Sonuç")
            pencerez.configure(background="black")
            dosya = open("katalog.txt", "r")
            veri = dosya.readlines()
            for i in veri:
                if (i.split('#')[0] == self.entryKitap.get()):
                    self.a=Label(pencerez,bg="black",fg="yellow",text="\nBulunan Kayıt: " + i)
                    self.a.grid()
                    hata = ""
                    break

                else:
                    hata="Aranan kayıt bulunamadı."
                    dosya.close()


        def yazar():
            pencerez = Tk()
            pencerez.wm_iconbitmap("turk.ico")
            baslik2 = pencerez.title("Aranılan Sonuç")
            pencerez.configure(background="black")
            dosya = open("katalog.txt", "r")
            veri = dosya.readlines()
            for i in veri:
                if (i.split('#')[1] == self.entryYazar.get()):
                    self.a = Label(pencerez,bg="black",fg="yellow",text="\nBulunan kayıt: " + i)
                    self.a.grid()
                    hata = ""
                    break
                else:
                    hata = "Aranan kayıt bulunamadı."


        def kitapTürü():
            pencerez = Tk()
            pencerez.wm_iconbitmap("turk.ico")
            baslik2 = pencerez.title("Aranılan Sonuç")
            pencerez.configure(background="black")
            dosya = open("katalog.txt", "r")
            veri = dosya.readlines()
            for i in veri:
                if (i.split('#')[2] == self.entryKitapTürü.get()):
                    self.a = Label(pencerez,bg="black",fg="yellow",text="\nBulunan kayıt: " + i)
                    self.a.grid()
                    hata = ""
                    break
                else:
                    hata = "Aranan kayıt bulunamadı."

        def ısbn():
            pencerez = Tk()
            pencerez.wm_iconbitmap("turk.ico")
            baslik2 = pencerez.title("Aranılan Sonuç")
            pencerez.configure(background="black")
            dosya = open("katalog.txt", "r")
            veri = dosya.readlines()
            for i in veri:
                if (i.split('#')[3] == self.entryIsbn.get()):
                    self.a = Label(pencerez,bg="black",fg="yellow",text="\nBulunan kayıt: " + i)
                    self.a.grid()
                    hata = ""
                    break
                else:
                    hata = "Aranan kayıt bulunamadı."

        def yayınevi():
            pencerez = Tk()
            pencerez.wm_iconbitmap("turk.ico")
            baslik2 = pencerez.title("Aranılan Sonuç")
            pencerez.configure(background="black")
            dosya = open("katalog.txt", "r")
            veri = dosya.readlines()
            for i in veri:
                if (i.split('#')[4] == self.entryYayınevi.get()):
                    self.a = Label(pencerez,bg="black",fg="yellow",text="\nBulunan kayıt: " + i)
                    self.a.grid()
                    hata = ""
                    break
                else:
                    hata = "Aranan kayıt bulunamadı."

        def Yayınyılı():
            pencerez = Tk()
            pencerez.wm_iconbitmap("turk.ico")
            baslik2 = pencerez.title("Aranılan Sonuç")
            pencerez.configure(background="black")
            dosya = open("katalog.txt", "r")
            veri = dosya.readlines()
            for i in veri:
                if (i.split('#')[5].strip() == self.entryYayınyılı.get()):
                    self.a = Label(pencerez,bg="black",fg="yellow",text="\nBulunan kayıt: " + i)
                    self.a.grid()
                    hata = ""
                    break
                else:
                    hata = "Aranan kayıt bulunamadı."

        self.labelKitap=Label(pencere4,bg="black",fg="yellow",text="Kitap İsmi ile Arama ")
        self.labelKitap.grid(row=0,column=0)
        self.entryKitap = Entry(pencere4,width="27")
        self.entryKitap.insert(0,"Kitap İsmi Giriniz...")
        self.entryKitap.grid(row=0,column=1)
        self.butonKitap=Button(pencere4,text="onay",bg="black",fg="yellow",cursor="star",font="bold",command=kitap)
        self.butonKitap.grid(row=0,column=2)

        self.labelYazar=Label(pencere4,bg="black",fg="yellow",text="Yazar İsimi ile Arama ")
        self.labelYazar.grid(row=1,column=0)
        self.entryYazar = Entry(pencere4,width="27")
        self.entryYazar.insert(0,"Yazar İsmi Giriniz...")
        self.entryYazar.grid(row=1,column=1)
        self.butonYazar = Button(pencere4, text="onay",bg="black",fg="yellow",cursor="star",font="bold",command=yazar)
        self.butonYazar.grid(row=1,column=2)

        self.labelKitapTürü=Label(pencere4,bg="black",fg="yellow",text="Kitap Türü ile Arama ")
        self.labelKitapTürü.grid(row=2,column=0)
        self.entryKitapTürü = Entry(pencere4,width="27")
        self.entryKitapTürü.insert(0, "Kitap Türü Giriniz...")
        self.entryKitapTürü.grid(row=2,column=1)
        self.butonKitapTürü = Button(pencere4, text="onay",bg="black",fg="yellow",cursor="star",font="bold",command=kitapTürü)
        self.butonKitapTürü.grid(row=2,column=2)

        self.labelIsbn=Label(pencere4,bg="black",fg="yellow",text="ISBN ile Arama ")
        self.labelIsbn.grid(row=3,column=0)
        self.entryIsbn = Entry(pencere4,width="27")
        self.entryIsbn.insert(0, "ISBN Giriniz...")
        self.entryIsbn.grid(row=3,column=1)
        self.butonIsbn = Button(pencere4, text="onay",bg="black",fg="yellow",cursor="star",font="bold",command=ısbn)
        self.butonIsbn.grid(row=3,column=2)

        self.labelYayınevi=Label(pencere4,bg="black",fg="yellow",text="Yayınevi ile Arama ")
        self.labelYayınevi.grid(row=4,column=0)
        self.entryYayınevi = Entry(pencere4,width="27")
        self.entryYayınevi.insert(0, "Yayınevi Giriniz...")
        self.entryYayınevi.grid(row=4,column=1)
        self.butonYayınevi = Button(pencere4, text="onay",bg="black",fg="yellow",cursor="star",font="bold",command=yayınevi)
        self.butonYayınevi.grid(row=4,column=2)

        self.labelYayınyılı=Label(pencere4,bg="black",fg="yellow",text="Yayın Yılı ile Arama ")
        self.labelYayınyılı.grid(row=5,column=0)
        self.entryYayınyılı = Entry(pencere4,width="27")
        self.entryYayınyılı.insert(0, "Yayın Yılı Giriniz...")
        self.entryYayınyılı.grid(row=5,column=1)
        self.butonYayınyılı = Button(pencere4, text="onay",bg="black",fg="yellow",cursor="star",font="bold",command=Yayınyılı)
        self.butonYayınyılı.grid(row=5,column=2)

    def hakkinda(self):
        hakkinda = Tk()
        hakkinda.title("Hakkında")
        hakkinda.wm_iconbitmap("turk.ico")
        hakkinda.geometry("160x180+260+195")
        hakkinda.resizable(width=FALSE, height=FALSE)
        Label(hakkinda, text="*Hacettepe Üniversitesi*\nBilgi ve Belge Yönetimi\n\n162\nProgramlama ve Algoritmalar\n\nEvren Aksuna\nBegüm Koçak\nMehmet Altay\nTarık Ünal\n",bg="black",fg="Yellow").pack()

root = Tk()
yeniPencere = Katalogum(root)
root.mainloop()