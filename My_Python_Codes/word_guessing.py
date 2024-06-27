kelime = "prospektüs"
can = 5
i = 0
tahmin = None

while i < len(kelime):
    if 0 < can:
        tahmin = input("Harf tahmininizi giriniz: ").lower()
        if tahmin == kelime[i]:
            tahmin = None
            i = i + 1 
        else:
            can = can -1
            if 0 < can:
                print("Girdiğiniz harf hatalıdır. Tekrar deneyiniz...") 
    else:
        print("Deneme hakkınız bitmiştir...")
        break

if i == len(kelime):
    print("Tebrikler kelimeyi buldunuz...")
    


