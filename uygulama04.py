#Begüm Koçak
#Şarkı sözü yazdırma

kadinadi = input("Bir kadın adı giriniz:")
erkekadi = input("Bir erkek adı giriniz:")
dortluk = int(input("Dortluk sayısı giriniz:"))

import random

sozler=[erkekadi + " ben sana mecburum " +
        kadinadi + "ben ölüyorum" + erkekadi + "seni anlamıyorum artık" +
        kadinadi + "benim için" + erkekadi + "yokluğun cehennemin öbür adıdır" + erkekadi + " özledim " +
        kadinadi + "ayrılıkta sevdaya dahil" + erkekadi + "ben sana mecburum" + kadinadi +
        " bu nasıl ayrılık" + erkekadi + "hüzün ve sevda" + kadinadi + "sen yoksun ya şimdi " + kadinadi +
        " esinirim"+ erkekadi + " mecburum" + kadinadi + " ne kadar seviyorsun dersen" + erkekadi +
        "o kadar işte,","mecburum" + kadinadi + "seviyorum" , "böyle bir sevmek görülmemiştir" + erkekadi + "benim için " +
        kadinadi + "hayat devam ediyor"]
for olusturulacak_sozler in sozler[:dortluk]:
    print(random.choice(sozler))

