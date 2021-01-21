"""
asal sayı bulma programı örnek
"""

def asal_sayi_bulo(sayi):
    sayi = int(sayi)
    if sayi == 1:
        return False
    elif sayi == 2:
        return True
    else:
        for i in range(2, sayi):
            if (sayi % i) == 0:
                return False
            return True

while True:
    sayi = input("Sayı(Çıkmak İçin q Bas):")

    if sayi == 'q':
        break
    else:
        if asal_sayi_bulo(sayi):
            print("Asal Sayı Buldunuz Tebrikler.")
        else:
            print("Sanırım Bu Sayı Asal Değil. Tekrar Deneyin...")







