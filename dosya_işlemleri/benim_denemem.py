# aile kitle endeksi, boy ortalaması ve kilo ortalaması
def aile(deger):
    deger = deger[:-1]
    li = deger.split(",")

    isim = li[0]
    yas = int(li[1])
    boy = int(li[2])
    kilo = int(li[3])
    endeks = kilo/(boy*boy)

    if endeks < 18.5:
        return isim + "------>" + ("Bedenn Kitle Endeksi: {} ve Durumunuz: '{}' ".format(endeks, "Zayıf")) + ("Yemenizi Biraz Arttırmanlısınız.....") + "\n"
    elif endeks > 18.5 and endeks < 25:
        return isim + "------>" + ("Bedenn Kitle Endeksi: {} ve Durumunuz: '{}' ".format(endeks, "Normal")) + ("Durumunuz Gayet İyi Tebrikler.....") + "\n"

    elif endeks > 25 and endeks < 30:
        return isim + "------>" + ("Bedenn Kitle Endeksi: {} ve Durumunuz: '{}' ".format(endeks, "Fazla Kilolu")) + ("Biraz Diyet Ve Spor Önerilir....") + "\n"

    elif endeks > 30:
        return isim + "------>" + ("Bedenn Kitle Endeksi: {} ve Durumunuz: '{}' ".format(endeks, "Obez")) + "Diyet Önerilir...." + "\n"

    else:
        return ("Hay Aksi Bir Sorun Oluştu.....")
    return





with open("bilgiler.txt", "r", encoding="utf-8") as file:
    liste = []
    for i in file:
        liste.append(aile(i))
with open("endeks.txt", "w", encoding="utf-8") as file2:
    for i in liste:
        file2.write(i)








