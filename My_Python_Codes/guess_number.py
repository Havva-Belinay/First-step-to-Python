import random

randomSayi = random.randint(0,200)

print('''Bilgisayar işlemcisinde 0 ile 200 arasında bir sayı tuttu.
Bu sayıyı tahmin etmeye çalışın :)''')
tahmin = int(input("Bilgisayarın işlemcisindeki sayı nedir? "))

while tahmin != randomSayi:
    if tahmin <= randomSayi:
        print("Daha büyük bir sayı giriniz...")
        tahmin = None
        tahmin = int(input("Tahmininiz: "))
    else:
        print("Daha küçük bir sayı giriniz...")
        tahmin = None
        tahmin = int(input("Tahmininiz: "))

print("Tebrikler... Doğru bildiniz...")
