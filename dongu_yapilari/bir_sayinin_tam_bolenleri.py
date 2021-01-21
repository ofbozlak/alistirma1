def sayi_tam_bol(sayi):
    sayi = int(sayi)
    lis = []
    for i in range(1, sayi+1):
        if sayi % i == 0:
            lis.append(i)
    return lis
while True:
    sayi = input("Sayı(Çıkmak İçin q Bas):")
    if sayi == 'q':
        break


    print("Sayının Tam Bölenleri:", sayi_tam_bol(sayi))




