i = 0
sonuc = list()
liste1 = [1, 2, 3, 4, 5, 6]
liste2 = [10, 20, 30, 40, 50, 60, 70]
while(i < len(liste1) and i < len(liste2)):

    sonuc.append((liste1[i], liste2[i]))
    i += 1

print(sonuc)
print("----------------------------------------")
print(list(zip(liste1, liste2)))  # zip fonksuyonu bizi yukarıdaki kod kalabalığındankurtardı.
print("----------------------------------------")
liste3 = ["Python", "Java", "Php", "Matlab", "Vivado", "Arduino"]
print(list(zip(liste1, liste2, liste3)))
print("----------------------------------------")
# iki liste üzerinde gezinmek için kullanılır.
for i, j in zip(liste1, liste3):
    print(i, "--->", j)













