def cift_sayi_bul(sayi):
    if((sayi % 2) == 0):
        return sayi
    else:
        return ValueError

liste = [10, 12, 1, 11, 21, 54, 104]

for i in liste:
    deger = cift_sayi_bul(i)
    try:
        print(deger)
    except ValueError:
        pass





