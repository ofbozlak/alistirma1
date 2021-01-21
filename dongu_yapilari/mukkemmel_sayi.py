"""Problem 1
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""
while True:
    girdi = input("mükkemmel sayıyı bulmaya çalışın(cikmak için q'a basın)...")
    if girdi == "q":
        break
    girdi= int(girdi)
    toplam = 0
    i = 1
    while(i < girdi):
        if((girdi % i) == 0):
            toplam += i
        i += 1
    if toplam == girdi:
        print("Bu Sayı Mükemmel Sayıdır Tebrikler...")
    else:
        print("Bu Sayı Mükemmel Sayı Değildir Lütfen Tekrar Deneyiniz")

















