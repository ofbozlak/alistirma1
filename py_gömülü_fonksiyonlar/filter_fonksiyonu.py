"""Bu konuda filter fonksiyonunu öğrenmeye çalışacağız.

filter(fonksiyon,iterasyon yapılabilen bir veritipi(liste vb.))

filter() fonksiyonu birinci parametre olarak mutlaka mantıksal değer dönen
(True , False) bir fonksiyon alır ve liste gibi veritiplerinin her bir elemanına bu fonksiyonunu uygular.
filter sadece True sonuç çıkaran değerleri alarak bir tane filter objesi döner. Hemen örneklerimize bakalım.
"""
liste1 = []
liste1 = list(filter(lambda x: x % 2 == 0, range(0, 10)))
print(liste1)
print("-----------------------------------")
# asal sayı bulan bir kod yazalım.
def asalsayı_bul(x):
    i = 2
    if(x == 1):
        return False
    elif(x == 2):
        return True
    else:

        while( x > i ):
            if(x % i == 0):
                return False
            i += 1
        return True
print(list(filter(asalsayı_bul, range(1,100))))







