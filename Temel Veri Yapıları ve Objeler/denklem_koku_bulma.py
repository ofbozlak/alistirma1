"""
denklem= ax^2+bx+c
kökleri ise

delta= b**2-4(a*c)
birinci kök= (-b-delta**0.5)/(2a)
ikinci kök= (-b+delata**0.5)/(2a)
"""
print("İkinci Dereceden Denklem Kökü Hesaplama")


a = int(input("Denklemin a değerini giriniz:"))
b = int(input("Denklemin b değerini giriniz:"))
c = int(input("Denklemin sabit değerini giriniz:"))

delta = b**2-4*(a*c)
birinci_kok = (-b-delta**0.5)/(2*a)
ikinci_kok = (-b+delta**0.5)/(2*a)

print("Birinci kök: {}\nİkinci kök: {}\n".format(birinci_kok,ikinci_kok))
print("İşlem bitmiştir....")




