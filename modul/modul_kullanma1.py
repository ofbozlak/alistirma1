import random
import time

print("""*****************************
  SAYI TAHMİN OYUNU BOLŞANS
*****************************
""")
rasgele_sayı = random.randint(1,40)

kullanıcı_hakkı = 6

while True:
    tahmin = int(input("Tahmin Ettiğiniz Sayı:"))
    if (tahmin < rasgele_sayı):
        print("işlem kontrol ediliyor....")
        time.sleep(1)
        print("biraz aşağıdan salladınız:))")
        kullanıcı_hakkı -= 1
    elif (tahmin > rasgele_sayı):
        print("işlem kontrol ediliyor....")
        time.sleep(1)
        print("biraz yukarıdan salladınız....")
        kullanıcı_hakkı -= 1
    else:
        print("işleminiz kontrol ediliyor...")
        time.sleep(1)
        print("Tebrikler doğru tahmin ")
        break
    if kullanıcı_hakkı == 0:
        print("Hakkınız bitmiştir daha sonra tekrar deneyiniz....")
        break























