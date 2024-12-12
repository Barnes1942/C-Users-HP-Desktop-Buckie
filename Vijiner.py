def vijiner_shifrlash(matn, kalit):
    shifrlangan_matn = ""
    kalit_length = len(kalit)

    for i in range(len(matn)):
        if matn[i].isalpha():  # faqat harflar bilan ishlaymiz
            offset = ord(kalit[i % kalit_length].lower()) - ord('a')
            shifrlangan_harf = chr((ord(matn[i].lower()) - ord('a') + offset) % 26 + ord('a'))
            shifrlangan_matn += shifrlangan_harf.upper() if matn[i].isupper() else shifrlangan_harf
        else:
            shifrlangan_matn += matn[i]  # belgilarni o'zgartirmasdan qo'shamiz

    return shifrlangan_matn


def vijiner_deshifrlash(shifrlangan_matn, kalit):
    deshifrlangan_matn = ""
    kalit_length = len(kalit)

    for i in range(len(shifrlangan_matn)):
        if shifrlangan_matn[i].isalpha():  # faqat harflar bilan ishlaymiz
            offset = ord(kalit[i % kalit_length].lower()) - ord('a')
            deshifrlangan_harf = chr((ord(shifrlangan_matn[i].lower()) - ord('a') - offset + 26) % 26 + ord('a'))
            deshifrlangan_matn += deshifrlangan_harf.upper() if shifrlangan_matn[i].isupper() else deshifrlangan_harf
        else:
            deshifrlangan_matn += shifrlangan_matn[i]  # belgilarni o'zgartirmasdan qo'shamiz

    return deshifrlangan_matn


def main():
    matn = input("Shifrlanishi kerak bo'lgan matnni kiriting: ")
    kalit = input("Kalitni kiriting: ")

    shifrlangan = vijiner_shifrlash(matn, kalit)
    print(f"Shifrlangan matn: {shifrlangan}")

    deshifrlangan = vijiner_deshifrlash(shifrlangan, kalit)
    print(f"Deshifrlangan matn: {deshifrlangan}")


if __name__ == "__main__":
    main()
