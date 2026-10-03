#variabel
vowel = "AIUEO"
vowel_map = {
"A": ['#', '*', '"', "!"],
"I": ['>', '/', '.', "@"],
"U": ['<', '[', '&', "%"],
"E": ['~', '`', '$', "£"],
"O": ['+', '-', '_', ")"]}
reverse_vowel_map = {}
for vowel, symbols in vowel_map.items():
 for symbol in symbols:
  reverse_vowel_map[symbol] = vowel

#Encrypt
def encrypt(teks, shift):

    hasil = ""
    position = 1

    for char in teks:
        if char.upper() in vowel:
            index = (position - 1) % 4
            encrypted = vowel_map[char.upper()][index]
            if char.isupper():
                hasil += "^"
            hasil += encrypted
            position += 1
        elif char.isalpha():
            if char.isupper():
                encrypted = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            else:
                encrypted = chr((ord(char) - ord("a") + shift) % 26 + ord("a") )
            hasil += encrypted
        else:
            hasil += char
    return hasil

#decrypt
def decrypt(teks, shift):

    hasil = ""
    uppercase_vowel = False

    for char in teks:
        if char == "^":
            uppercase_vowel = True
            continue
        if char in reverse_vowel_map:
            decrypted = reverse_vowel_map[char]
            if uppercase_vowel:
                decrypted = decrypted.upper()
                uppercase_vowel = False
            else:
                decrypted = decrypted.lower()
        elif char.isalpha():
            if char.isupper():
                decrypted = chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
            else:
                decrypted = chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
        else:
            decrypted = char
        hasil += decrypted
    return hasil

#inputan
teks = input("Masukkan teks: ")
pilihan = input("Pilih operasi (E/D): ").upper()
while True:
            try:
                shift = int(input("Masukkan shift: "))
                if shift >= 0:
                 break
                else:
                 print("Shift tidak boleh negatif.")
            except ValueError:
                print("Masukkan angka yang valid.")
if pilihan == "E":
    hasil= encrypt(teks, shift)
    print(hasil)

elif pilihan == "D":
    hasil = decrypt(teks, shift)
    print(hasil) 