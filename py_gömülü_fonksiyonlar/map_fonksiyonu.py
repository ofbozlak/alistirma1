"""-----------Map Fonksiyonu-------------------
Bu konuyla beraber Pythonda gömülü olan bazı fonksiyonlarımızı öğrenmeye başlıyoruz.

Pythonda gömülü bir fonksiyon olan map() fonksiyonunun yapısı şu şekildedir.

                map(fonksiyon,iterasyon yapılabilecek veritipi(liste,demet vb),....)

map() fonksiyonu ilk parametre olarak bir tane fonksiyon objesi alır.
(Fonksiyonlar da birer obje olduğu için başka bir fonksiyona gönderilebilir.)
2. parametre olarak da bir tane iterasyon yapılacak veritipi alarak ,
gönderilen fonksiyonu her bir eleman üzerinde uygulayarak sonuçları bir map objesi olarak döner.
Örneklerimize geçersek bu fonksiyonun işlevini daha iyi anlayacağız.
"""

def carp(x):
    return x * 2
liste = list(map(carp,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # liste gönderdik.
print(liste)
#  --------------------------------------------------------------
print("----------------------------------------------------")
li = list(map(lambda x: x**2, (1, 2, 3, 4, 5, 6, 7, 8,  9, 10)))  # demet gönderdik.
print(li)
#  ------------------------------------------------------------
print("-----------------------------------------------")
liste1 = [1, 2, 3, 4, 5, 6]
liste2 = [10, 11, 12, 13]
liste3 = [21, 22, 13]
print(list(map(lambda x, y, z: x*y+z, liste1, liste2, liste3)))  # eşit olmayan listede eşit olduğu yere kadar işlem yapılır.
#  -------------------------------------------------------------------
print("-------------------------------------------------------")






