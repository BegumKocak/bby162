#Begüm Koçak
#zıt anlamlamlı kelimeleri liste ve sözlük şeklinde gösterme.

zıtanlam1={"acı":"tatlı", "hızlı":"yavaş", "hüzün":"sevinç", "ucuz":"pahalı","güzel":"çirkin","zengin":"fakir"}
print(zıtanlam1)
print(zıtanlam1.keys())# 1.ciler
print(zıtanlam1.values())# 2.ciler
print("açık" in zıtanlam1)#sözlükte olup olmadığı
zıtanlam1["açık"]="kapalı" #sözlüğe ekleme
print("açık" in zıtanlam1)#sözlükte olup olmadığı
print(zıtanlam1["acı"])#1.söyleyip karşılığını söyleme


zıtanlam2=["acı","hızlı","hüzün","ucuz","güzel"]
print(zıtanlam2)
zıtanlam2+=("zengin")#sabit ekleme
print(zıtanlam2)
zıtanlam2.append("zıt anlamlı kelimeler")#en sona ekleme
print(zıtanlam2)