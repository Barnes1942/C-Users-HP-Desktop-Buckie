def affine_encrypt(plaintext, a, b):
    m = 26
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            x = ord(char) - ascii_offset
            encrypted_char = (a * x + b) % m
            ciphertext += chr(encrypted_char + ascii_offset)
        else:
            ciphertext += char

    return ciphertext


def affine_decrypt(ciphertext, a, b):
    m = 26
    plaintext = ""

    # Multiplikativ kalit uchun inversni hisoblash
    a_inv = pow(a, -1, m)

    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            y = ord(char) - ascii_offset
            decrypted_char = (a_inv * (y - b)) % m
            plaintext += chr(decrypted_char + ascii_offset)
        else:
            plaintext += char

    return plaintext


# Konsoldan qiymatlarni olish
plaintext = input("Shifrlanishi kerak bo'lgan matnni kiriting: ")
a = int(input("Multiplikativ kalit (a) ni kiriting: "))
b = int(input("Qoshish kaliti (b) ni kiriting: "))

# Shifrlash
ciphertext = affine_encrypt(plaintext, a, b)
print("Shifrlangan matn:", ciphertext)

# Deshifrlash
decrypted_text = affine_decrypt(ciphertext, a, b)
print("Deshifrlangan matn:", decrypted_text)
