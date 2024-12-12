#USR/user/bin
def sezar_shifrlash(matn, kalit):
    shifrlangan_matn = ""
    for harf in matn:
        if harf.isalpha():
            start = ord('A') if harf.isupper() else ord('a')
            shifrlangan_harf = chr((ord(harf) - start + kalit) % 26 + start)
            shifrlangan_matn += shifrlangan_harf
        else:
            shifrlangan_matn += harf
    return shifrlangan_matn
def sezar_deshifrlash(matn, kalit):
    return sezar_shifrlash(matn, -kalit)
matn = input("Shifrlash uchun matn kiriting: ")
kalit = int(input("Kalitni kiriting (1-25): "))
shifrlangan_matn = sezar_shifrlash(matn, kalit)
print("Shifrlangan matn:", shifrlangan_matn)
deshifrlangan_matn = sezar_deshifrlash(shifrlangan_matn, kalit)
print("Deshifrlangan matn:", deshifrlangan_matn)
