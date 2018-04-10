import random
hak = 3
i = 0
kelimeler = random.choice(["telefon","telgraf","internet","televizyon","gazete"])
kelimeklavuzu = []
for a in kelimeler:
    kelimeklavuzu.append("-")
print(kelimeklavuzu)


while hak > 0:
    alınanharf = input("\nBir harf giriniz: ")
    if alınanharf in kelimeler:
        for kontrolet in kelimeler:
            if kelimeler [i] == alınanharf:
                kelimeklavuzu [i] = alınanharf
            i+=1
        print(kelimeklavuzu)
        i=0



    else:
        i=0
        hak-=1
        print('Yanlış harf girdiniz. Kalan hakkınız: {}'.format(hak))

if hak == 0:
    print('Oyunu kaybettiniz. Doğru kelime "{}".\n'.format(kelimeler))



    


