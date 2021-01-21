liste = ["Elma", "Muz", "Kiraz", "Kivi", "Ananas"]
i = 0
sonuc = []
while (i < len(liste)):
    sonuc.append((i, liste[i]))
    i += 1
print(sonuc)
print("-------------------------------------")
# yukarıda yapılan işi aşağıdaki tek satır kod yapıyor.

print(list(enumerate(liste)))




