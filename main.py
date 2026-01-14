# 1-misol

summa = int(input("summani kiri: "))

if summa < 0:
    if summa > 50000:
        print("chegirma yoq")
    elif summa < 100000:
        print("5% chegirma")
    elif summa < 200000:
        print("10% chergirma")
    else:
        print("15% chegirma")
else:
    print("manfiy sonlarga ruxsat yoq")


# 2-misol

yol = input("yol va svetafor holatini kirit: ")

if yol == "qizil":
    print("to'xtang ")
elif yol == "sariq":
    print("tayyorlaning")
else:
    print("yuring")
    if yol == "bosh":
        print("yuring")
    elif yol == "band":
        print("kutib turing")

# 3-misol

dori = int(input("hozirgi vaqtini kiriting: "))

if 6 < dori < 11:
    print("ertablki dori")
elif 12 < dori < 17:
    print("kunduzgi dori")
elif 18 < dori < 23:
    print("kechgi dori")
else:
    print("dori ichish kera emas")

# 4-misol

harorat = int(input("hozirgi haroratni kirit: "))

if harorat < 0:
    print("palto, qolqop kiying")
elif harorat < 15:
    print("jaket kiying")
elif harorat < 25:
    print("futbolka yetarli")
else:
    print("yengil kiyim, soyaban oling")

# 5-misol

sinf = int(input("sinfingizni kiriting: "))
massa = float(input("sumka ogirligi: "))

if 1 <= sinf <= 4 and massa >= 2:
    print("ogirlikni kamaytiring")
elif 5 <= sinf <= 9 and massa >= 4:
    print("ogirlikni kamaytiring")
else:
    print("normal")
