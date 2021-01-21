print("""****************************************
FAKTORİYEL BULMA PROGRAMINA HOS GELDİNİZ
****************************************
""")
while True:
    girilen_sayi = input("Factoriyel i alinacak sayı(cikmak için q' ya basınız):")
    if girilen_sayi == "q":
        print("programdan cıkış yapılıyor....")
        break
    carpim = 1
    girilen_sayi = int(girilen_sayi)
    for i in range(2, girilen_sayi+1):
        carpim *= i
    print("Girdiğiniz Sayının Factoriyeli: {}".format(carpim))














