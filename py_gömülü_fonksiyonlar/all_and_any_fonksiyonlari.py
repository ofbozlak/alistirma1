# bir liste içersinde bütün değerler true ise soınucu true döndüren bir fonksiyon yaz
def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True
liste1 =[True, True, False, True, False]

print(hepsi(liste1))

print("-----------------")
# bu fonksiyon için all gömülü fonksiyonu kullanılır.

print(all(liste1))

# içersinde en az bir tane True olması durumunda True değeri dönen bir fonksiyn yaz.
def en_az_biri(liste):
    for i in liste:
        if i:
            return True
    return False

print("-----------------")
print(en_az_biri(liste1))
print("--------------")
# bu fonksiyon için any vardır.
print(any(liste1))





