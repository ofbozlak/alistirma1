"""class Çalışan():   # Inheritance (kalıtım)
    def __init__(self, isim, soyisim, maaş, departman):
        print("çalışan sınıfının init fonksiyonu")

        self.isim = isim
        self.soyisim = soyisim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigöster(self):
        print("bilgiler gösteriliyor.....")
        print("İsim: {}\nSoyisim: {}\nMaaş: {}\ndepartman: {}\n".format(self.isim, self.soyisim, self.maaş, self.departman))
    def demparmandeğiştir(self, yeni_departman):
        self.departman = yeni_departman
class Yönetici(Çalışan):
    pass

yönetici = Yönetici("ömer","Bozlak",3000,"bilişim")

yönetici.bilgilerigöster()"""

"""class Çalışan():   # bilgi ekleme
    def __init__(self, isim, soyisim, maaş, departman):
        print("çalışan sınıfının init fonksiyonu")

        self.isim = isim
        self.soyisim = soyisim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigöster(self):
        print("bilgiler gösteriliyor.....")
        print("İsim: {}\nSoyisim: {}\nMaaş: {}\ndepartman: {}\n".format(self.isim, self.soyisim, self.maaş, self.departman))
class Yönetici(Çalışan):
    def zam_yap(self, zam_miktarı):
        print(" Zam Yapılıyor.....")
        self.maaş += zam_miktarı
yönetici1 = Yönetici("Ömer","Faruk",3500,"Onarım")

yönetici1.zam_yap(500)

yönetici1.bilgilerigöster()"""

"""class Çalışan():   # Overriding (İptal Etme)
    def __init__(self, isim, soyisim, maaş, departman):
        print("çalışan sınıfının init fonksiyonu")

        self.isim = isim
        self.soyisim = soyisim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigöster(self):
        print("bilgiler gösteriliyor.....")
        print("İsim: {}\nSoyisim: {}\nMaaş: {}\ndepartman: {}\n".format(self.isim, self.soyisim, self.maaş, self.departman))

class Yönetici(Çalışan):
    def __init__(self, isim, soyisim, maaş, departman, kişi_sayısı):
        print("Yönetici sınıfının init fonksiyonu")
        self.isim = isim
        self.soyisim = soyisim
        self.maaş = maaş
        self.departman = departman
        self.kişi_sayısı = kişi_sayısı
    def bilgilerigöster(self):
        print("bilgiler gösteriliyor.....")
        print("İsim: {}\nSoyisim: {}\nMaaş: {}\ndepartman: {}\nSorumlu Olduğu Kişi: {}".format(self.isim, self.soyisim, self.maaş, self.departman, self.kişi_sayısı))

    def zam_yap(self, zam_miktarı):
        print(" Zam Yapılıyor.....")
        self.maaş += zam_miktarı


yönetici2 = Yönetici("Ömer", "Bozlak", 2000, "Üretim", 15)

yönetici2.zam_yap(1000)

yönetici2.bilgilerigöster()"""

class Çalışan(): #super anahtar kelimesi
    def __init__(self, isim, soy_isim, maaş, departman):
        print("çalışan sinifinin inir fonksiyonu....")
        self.isim = isim
        self.soy_isim = soy_isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigöster(self):
        print("Bilgiler gösteriliyor...")
        print("İsim: {}\nSoy İsim: {}\nMaaş: {}\nDepartman: {}\n".format(self.isim, self.soy_isim, self.maaş, self.departman))

    def zamn_yap(self, zamn_miktarı):
        print("Zam yapılıyor....")
        self.maaş += zamn_miktarı

class Yönetici(Çalışan):
    def __init__(self,isim, soy_isim, maaş, departman, kişi_sayısı):
        super().__init__(isim, soy_isim, maaş, departman)
        print("Yönetici sınıfının init fonksiyonu....")
        self.kişi_sayısı = kişi_sayısı
    def bilgilerigöster(self):
        print("Yönetici  sınıfının bilgileri gösteriliyor...")
        print("İsim: {}\nSoy İsim: {}\nMaaş: {}\nDepartman: {}\nSorumlu olduğu kişi sayısı: {}".format(self.isim, self.soy_isim, self.maaş, self.departman, self.kişi_sayısı))
    def zam_yap(self, zam_miktarı):
        print("zam yapılıyor.....")
        self.maaş += zam_miktarı
yönetici5 = Yönetici("Ömer","Faruk",4000,"müdür",150)
yönetici5.zam_yap(500)
yönetici5.bilgilerigöster()





