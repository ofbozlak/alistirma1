class Kitap():
    def __init__(self,kitap_adi,yazar,sayfa_sayisi,tur):
        print("init fonksiyonu çalıştı....")
        self.kitap_adi = kitap_adi
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur
    def __str__(self):
        return "Kitap Adı: {}\nYazarı: {}\nSayfa Sayısı: {}\nTürü: {}\n".format(self.kitap_adi,self.yazar,self.sayfa_sayisi,self.tur)
    def __len__(self):
        return self.sayfa_sayisi
    def __del__(self):
        print("kitap classı siliniyor....")


kitap = Kitap("BEŞİNCİ TÜP","MISHAEL PALMER",472,"POLİSİYE")

print(kitap)
print(len(kitap))
del(kitap)

