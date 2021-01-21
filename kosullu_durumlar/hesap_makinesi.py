print("""***************************
HESAP MAKİNESİ UYGULAMASI
İşlemler;
1. İşlem: Toplama
2. İşlem: Çıkarma
3. İşlem: Çarpma
4. İşlem: Bölme
***************************
""")
a = int(input("Birinci Sayıyı Giriniz:"))
b = int(input("İkinci Sayıyı Giriniz:"))

iş = input("yapmak istediğiniz işlemi seçiniz:")

if iş == "1":
    print("{} ile {} inin toplamı {}'dır.".format(a, b, a+b))
elif iş == "2":
    print("{} ile {} inin farkı {}'dır.".format(a, b, a-b))
elif iş == "3":
    print("{} ile {} inin carpımı {}'dır.".format(a, b, a*b))
elif iş == "4":
    print("{} ile {} inin bölümü {}'dır.".format(a, b, a/b))
else:
    print("geçersiz işlem....")
