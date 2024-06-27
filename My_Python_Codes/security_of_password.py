parola = input("Parolayı giriniz: ")

def uzunluk(parola):
    if len(parola) >= 8:
        return 1
    else:
        return 0
def sayı(parola):
    if any(char.isdigit() for char in parola):
        return 1
    else:
        return 0
def boyut(parola):
    if any(char.isupper() for char in parola):
        return 1
    else:
        return 0
def specual(parola):
    if any(not char.isalnum() for char in parola):
        return 1
    else:
        return 0

uzunluk1 = uzunluk(parola)
sayı1 = sayı(parola)
boyut1 = boyut(parola)
specual1 = specual(parola)

parola_power = uzunluk1 + sayı1 + boyut1 + specual1

if parola_power == 4:
    print("Parolanız güçlü...")
elif 2 <= parola_power < 4:
    print("Parolanız orta seviyede güçlü...")
else:
    print("Parolanız güçlü değil...")