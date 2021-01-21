"""
Kodlama egzersizimizde bir sınıfın harf notlarını hesapladığımız programı geliştirerek kalanları "kalanlar.txt" dosyasında ve
geçenleri "geçenler.txt" dosyasına yazmaya çalışın.
"""
def not_hesapla(deger):

    deger = deger[:-1]
    liste = deger.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    ort = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (ort >= 90):
        harf = "AA"
    elif(ort >= 85):
        harf = "BA"
    elif(ort >= 80):
        harf = "BB"
    elif(ort >= 70):
        harf = "CA"
    elif(ort >= 65):
        harf = "CB"
    elif(ort >= 60):
        harf = "CC"
    elif(ort >= 50):
        harf = "DC"
    elif(ort >= 40):
        harf = "DD"
    else:
        harf = "FF"

    return isim + "------>" + harf + "\n"

with open("dosya.txt", "r", encoding="utf-8") as file:

    harf_notu_listesi = []

    for i in file:

        harf_notu_listesi.append(not_hesapla(i))

with open("harf_notu.txt", "w", encoding="utf-8") as file2:

    for i in harf_notu_listesi:
        file2.write(i)




