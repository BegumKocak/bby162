#Begüm Koçak
#Şarkı sözü yazdırma

kadinadi = input("Bir kadın adı giriniz:")
print(kadinadi)
erkekadi = input("Bir erkek adı giriniz:")
print(erkekadi)
mısra = int(input("Mısra sayısı giriniz:"))
print(mısra)

sozler=[erkekadi + " ben sana mecburum "+ kadinadi +" ben ölüyorum", "seni anlamıyorum artık" + kadinadi + "benim için","yokluğun cehennemin öbür adıdır", erkekadi + " özledim " + kadinadi + "ayrılıkta sevdaya dahil","ben sana mecburum" + kadinadi + " bu nasıl ayrılık","hüzün ve sevda", "sen yoksun ya şimdi " + kadinadi + " esinirim" + erkekadi + " mecburum" + kadinadi + " ne kadar seviyorsun dersen,","o kadar işte,","mecburum,","seviyorum,","böyle bir sevmek görülmemiştir","benim için " + kadinadi + " hayat devam ediyor"]
for olusturulacak_sozler in sozler[:mısra]:
    print(olusturulacak_sozler)


if mısra > 11:
    print("Geçerli bir mısra sayısı giriniz:")

