"""reduce() fonksiyonu değer olarak aldığı fonksiyonu soldan başlayarak listenin ilk 2 elemanına uygular
ve daha sonra çıkan sonucu listenin 3. elemanına uygular ve bu şekilde devam ederek liste bitince bir tane değer döner.
Anlamak için örneğimize ve görselimize bakalım."""
from functools import reduce
def toplam(x, y):
    return x+y
liste = [1, 2, 3, 4, 5]

print(reduce(toplam, liste))
print("--------------------------------------")
# reduce yardımıyla bir listenin en büyük sayısını bulma

def max(x, y):
    if( x > y ):
        return x
    else:
        return y
print(reduce(max,liste))

# reduce fonksiyonu sayesinde factöriel de hesaplanabilir.



