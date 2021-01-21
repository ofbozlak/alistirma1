"""Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
 """
print("Bedenn Kitle Endeksi Hesaplama ")
kilo = int(input("Kilonuzu giriniz(kg):"))
boy = float(input("Boyunuzu giriniz(m):"))
endeks = kilo/(boy*boy)

if endeks < 18.5:
    print("Bedenn Kitle Endeksi: {} ve Durumunuz: {}".format(endeks, "Zayıf"))
    print("Yemenizi Biraz Arttırmanlısınız.....")
elif endeks > 18.5 and endeks < 25:
    print("Bedenn Kitle Endeksi: {} ve Durumunuz: {}".format(endeks, "Normal"))
    print("Durumunuz Gayet İyi Tebrikler.....")
elif endeks > 25 and endeks < 30:
    print("Bedenn Kitle Endeksi: {} ve Durumunuz: {}".format(endeks, "Fazla Kilolu"))
    print("Biraz Diyet Ve Spor Önerilir....")
elif endeks > 30:
    print("Bedenn Kitle Endeksi: {} ve Durumunuz: {}".format(endeks, "Obez"))
    print("Diyet Önerilir....")
else:
    print("Hay Aksi Bir Sorun Oluştu.....")
