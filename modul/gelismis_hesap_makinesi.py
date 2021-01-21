"""                             Proje 1
Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın.
"""
import math
print("""
*************************************
BİLİMSEL HESAP MAKİNESİNE HOŞGELDİNİZ
İŞLEMLER;
1-)acos
2-)acosh
3-)asin
4-)asinh
5-)atan
6-)atan2
7-)atanh
8-)ceil
9-)exp
10-)floor
11-)cos
12-)cosh
13-)sin
14-)sinh
15-)sqrt
16-)tan
17-)log10
18-)pow
*************************************
""")
while True:
    print("Çıkmak İçin q'ya Basınız!!!")
    islem = input("Bir İşlem Giriniz:")
    if islem == "q":
        print("Programdan Çıkılıyor.")
        break
    elif islem == "1":
        """
        acos(x, /)
        Return the arc cosine (measured in radians) of x.
        """
        x = float(input("acos Alınacak Değeri Giriniz:"))
        y = math.acos(x)
        print("SONUÇ= {}".format(y))
    elif islem == "2":
        """
        acosh(x, /)
        Return the inverse hyperbolic cosine of x.
        """
        x = float(input("acosh Alınacak Değeri Giriniz:"))
        y = math.acosh(x)
        print("SONUÇ= {}".format(y))
    elif islem == "3":
        """
        asin(x, /)
        Return the arc sine (measured in radians) of x.
        """
        x = float(input("asin Alınacak Değeri Giriniz:"))
        y = math.asin(x)
        print("SONUÇ= {}".format(y))
    elif islem == "4":
        """
        asinh(x, /)
        Return the inverse hyperbolic sine of x..
        """
        x = float(input("asinh Alınacak Değeri Giriniz:"))
        y = math.asinh(x)
        print("SONUÇ= {}".format(y))
    elif islem == "5":
        """
        atan(x, /)
        Return the arc tangent (measured in radians) of x.
        """
        x = float(input("atan Alınacak Değeri Giriniz:"))
        y = math.atan(x)
        print("SONUÇ= {}".format(y))
    elif islem == "6":
        """
        atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.

        Unlike atan(y/x), the signs of both x and y are considered..
        """
        x = float(input("atan2 y Değeri Giriniz:"))
        z = float(input("atan2 x Değeri Giriniz:"))
        y = math.atan2(z, x)
        print("SONUÇ= {}".format(y))
    elif islem == "7":
        """
        atanh(x, /)
        Return the inverse hyperbolic tangent of x.
        """
        x = float(input("atanh Alınacak Değeri Giriniz:"))
        y = math.atanh(x)
        print("SONUÇ= {}".format(y))
    elif islem == "8":
        """
        ceil(x, /)
        Return the ceiling of x as an Integral.
        """
        x = float(input("Ceil Alınacak Değeri Giriniz:"))
        y = math.ceil(x)
        print("SONUÇ= {}".format(y))
    elif islem == "9":
        """
        exp(x, /)
        Return e raised to the power of x.
        """
        x = float(input("exp Alınacak Değeri Giriniz:"))
        y = math.exp(x)
        print("SONUÇ= {}".format(y))
    elif islem == "10":
        """
        floor(x, /)
        Return the floor of x as an Integral.

        This is the largest integer <= x.
        """
        x = float(input("floor Alınacak Değeri Giriniz:"))
        y = math.floor(x)
        print("SONUÇ= {}".format(y))
    elif islem == "11":
        """
        cos(x, /)
        Return the cosine of x (measured in radians).
        """
        x = float(input("cos Alınacak Değeri Giriniz:"))
        y = math.cos(x)
        print("SONUÇ= {}".format(y))
    elif islem == "12":
        """
        cosh(x, /)
        Return the hyperbolic cosine of x.
        """
        x = float(input("cosh Alınacak Değeri Giriniz:"))
        y = math.cosh(x)
        print("SONUÇ= {}".format(y))
    elif islem == "13":
        """
        sin(x, /)
        Return the sine of x (measured in radians).
        """
        x = float(input("sin Alınacak Değeri Giriniz:"))
        y = math.sin(x)
        print("SONUÇ= {}".format(y))
    elif islem == "14":
        """
        sinh(x, /)
        Return the hyperbolic sine of x.
        """
        x = float(input("sinh Alınacak Değeri Giriniz:"))
        y = math.sinh(x)
        print("SONUÇ= {}".format(y))
    elif islem == "15":
        """
        sqrt(x, /)
        Return the square root of x.
        """
        x = float(input("sqrt Alınacak Değeri Giriniz:"))
        y = math.sqrt(x)
        print("SONUÇ= {}".format(y))
    elif islem == "16":
        """
        tan(x, /)
        Return the tangent of x (measured in radians).
        """
        x = float(input("tan Alınacak Değeri Giriniz:"))
        y = math.tan(x)
        print("SONUÇ= {}".format(y))
    elif islem == "17":
        """
        log10(x, /)
        Return the base 10 logarithm of x.
        """
        x = float(input("log10 Alınacak Değeri Giriniz:"))
        y = math.log10(x)
        print("SONUÇ= {}".format(y))
    elif islem == "18":
        """
        pow(x, y, /)
        Return x**y (x to the power of y).
        """
        x = float(input("x Değerini Giriniz:"))
        z = float(input("y Değerini Giriniz:"))
        y = math.pow(x, z)
        print("SONUÇ= {}".format(y))
    else:
        print("yanlış bir işlem yaptınız tekrar deneyin....")



















