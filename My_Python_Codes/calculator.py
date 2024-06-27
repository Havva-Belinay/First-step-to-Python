
sayi1 = int(input("Birinci sayıyı giriniz: "))
islem = input("yapmak istediğiniz işlemi seçiniz: +, -, *, /: ")
sayi2 = int(input("ikinci sayıyı giriniz: "))

if islem == "+":
      print("Sonuç:" + str(sayi1 + sayi2))
elif islem == "-":
      print("Sonuç: " + str(sayi1 - sayi2))
elif islem == "*":
      print("Sonuç: " + str(sayi1 * sayi2))
elif islem == "/":
      print("Sonuç: " + str(sayi1 / sayi2))
else:
      print("Hatalı istek gönderdiniz...")
