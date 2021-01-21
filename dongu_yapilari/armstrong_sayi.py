"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı
( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""
while True:
    print("Çıkmak İçin '1' Bas")
    sayi = input("Armstrong Saysını Bul(4 basamaklı sayı girin):")
    if sayi == '1':
        break
    deger = 0
    for i in sayi:
        i = int(i)
        deger += i**4
    deger = str(deger)
    if deger == sayi:
        print("Tebrikler Sayıyı Buldunuz....")
    else:
         print("Tekrar Deneyiniz....")











