print("Adam Asmaca oyununa hoş geldiniz.")
import random
şehirler = random.choice(['ankara', 'izmir', 'adana', 'kütahya', 'antalya', 'istanbul'])
harfhavuzu = []
kalanhak = 4
karakterçizgisi = '_'
karakteryazısı = list(karakterçizgisi * len(şehirler))
dongu = 1


while dongu:
    print(' '.join(karakteryazısı), end='\n\n')
    alinanharf = input('Bir harf giriniz: ')
    try:
        int(alinanharf)
        print('Doğru bir şeyler girdiğinden emin olunuz.')
    except:
        if len(alinanharf) > 1:
            print('Sadece bir harf giriniz.')
        else:
            if alinanharf in harfhavuzu:
                print('Bu harfi zaten girdiniz.')


            else:
                bulduk = None
                for i in range(len(şehirler)):
                    if alinanharf == şehirler[i]:
                        bulduk = True
                        karakteryazısı[i] = alinanharf
                        harfhavuzu.append(alinanharf)
                        if karakterçizgisi not in karakteryazısı:
                            print(' '.join(karakteryazısı))
                            print('Tebrikler kelimeyi buldunuz.')
                            dongu = 0


                else:
                    if bulduk != True:
                        kalanhak -= 1
                        print('Yanlış harf girdiniz. Kalan hakkınız: {}'.format(kalanhak))
                        harfhavuzu.append(alinanharf)
                if kalanhak == 0:
                    print('Kaybettiniz. Doğru kelime "{}"'.format(şehirler))
                    break










