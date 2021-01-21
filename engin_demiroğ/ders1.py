baslik = "İlginiz çekebilir!!!!"
vade = 45
faizOrani = 1.69

#  ---------------------------


print(baslik)
print("Vade: ", vade)
print("Faiz Oranı: {}".format(faizOrani))
print(type(faizOrani))
print(type(vade))
print(type(baslik))

print("""
         |
         |
         |
        \ /
""")

#  --------------------------------------

bistDun = 7.35
bistBugun = float(input("Bist Bugün'ü Girin:"))

if( bistDun > bistBugun ):
    print("Azalma Varrr!!!")
elif(bistDun == bistBugun):
    print("Eşit !!!!")
else:
    print("Artma var!!!!")
# ------------------------------------------
kredi1 = "Hılzlı kradi"
kredi2 = "Mutlu emekli"

liste = ["hızlı kredi", "maasini halkbanktan alan", "mutlu emekli"]
for i in liste:
    print(i)
print("---------------------------------------------------------------")
for i in range(0, len(liste)):
    print(liste[i])

# --------------------------------------------------------------------------------







