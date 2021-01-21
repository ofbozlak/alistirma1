"""hatalar var düzenle......"""


print("kullanıcı girişinehoş geldiniz...")
kull = "ömer"
par = "12345"

while(True):
    print("çıkmak için 1 e basınız")
    a = input("kullanıcı isminizi giriniz:")
    if kull == a:
        while(True):
            parola = input("parolanızı giriniz(çikmak için q ya basınız):")
            if par == parola:
                print("programa hoşgeldiniz....")
                break
            elif parola == "q":
                break
            else:
                print("parola yanlış tekrar nedeyiniz....")
    elif a == "1":
        break
    else:
        print("yanlış giriş yaptınız lütfen tekrar deneyiniz:")
