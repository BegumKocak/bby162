number= int(input("saniye gir:"))

d=int(number/60)
remainder= number%60
s= int(d/60)

print("dakika,""saniye=" + str(d),str(remainder))
print("saat="+ str(s))

g=int(s/24)
a=int(g/30)

print("gün=" + str(g))
print("a=" + str(a))

y=int(a/12)

print("yıl=" + str(y))
