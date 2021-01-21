"""dosya açma kapatma ve üzerine yazma işlemleri"""

file = open("deneme.txt", "w", encoding="utf-8")   # w sadece yazma da kullanılır eğer dosya varsa içindekileri silip tekrar oluşturur.
file.write("Ömer Faruk Bozlak\n")
file.write("Faruk Bozlak\n")
file.close()
file = open("deneme.txt", "a", encoding="utf-8")   # a ekleme için kullanılır.
file.write("Ömer Bozlak")
file.close()
print("---------------------------------------------------")

"""dosyadan okuma işlemi yapma"""
file = open("deneme.txt", "r", encoding="utf-8")    # okuma işlemi için kullanılır.

for i in file:
    print(i, end="")
file.close()
try:
    file = open("deneme1.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("\nAradığınız Dosya Bulunamadı....")

try:
    file = open("deneme.txt", "r", encoding="utf-8")
    print(file.read())
    print(file.read())  # burada imleç en sonda olduğu için ikinci bir okuma yapmıyor.
    file = open("deneme.txt", "r", encoding="utf-8")
    print(file.readline())  # tek satır okuyor.  ve  birer boşluk bırakıyor.
    print(file.readlines())  # okuduğu değerleri bir listeye atıyor.
except FileNotFoundError:
    print("\nAradığınız Dosya Bulunamadı....")

file.close()
print("---------------------------------------------------------")
# dosya'yı otomatik kapatma
with open("deneme.txt", "r", encoding="utf-8") as file:
    for i in file :
        print(i, end="")
print("\n----------------------------------------------------------")
print("\nİmleç İşlemleri:")
with open("deneme.txt", "r", encoding="utf-8") as file:
    print(file.tell())  # .tell() fonksiyonu okuma yapan imleçin bize nerede olduğunu gösterir.
    print(file.seek(6))  # .seek fonksiyonu ise imleç i istediğimiz yere getirmemizi sağlar.
    print(file.read(6))   # imleçin olduğu yerden 6 byt okumamızı sağlar.
print("-----------DOSYALARDA DEĞĞİŞİKLİK YAPMA----------------")
with open("deneme.txt", "r+", encoding="utf-8") as file:  # r+ hem okuma hemde yazma yapmamızı sağlar.
    ekle  = file.read()
    ekle = "Neden Olmuyor\n" + ekle
    file.seek(0)
    print(ekle)
with open("deneme.txt", "a", encoding="utf-8") as file:
    file.write("\nŞimdi Oldu\n")
with open("deneme.txt", "r+", encoding="utf-8") as file:
    print("--------")
    print(file.read())
with open("deneme.txt", "r+", encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(3, "bakalım oldu mu?\n")
    file.seek(0)
    for i in liste:
        file.write(i)   # file.writelines(liste) ile de aynı işlem yapılabilir.
    file.seek(0)
    print(file.read())







