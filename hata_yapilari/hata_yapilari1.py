try:
    a = int(input("sayi1:"))
    b = int(input("sayi2:"))
    print(a/b)
except ValueError:
    print("lütfen iki tane sayı giriniz!!!")
except ZeroDivisionError:
    print("Bir Sayı 0'a bölünemez .....")

print("İşlem Bitmiştir!!!")

