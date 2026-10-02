
vowels = "AIUEO"
position = 1
vowel_map = {
"A": ['#', '*', '"', "!"],
"I": ['>', '/', '.', "@"],
"U": ['<', '[', '&', "%"],
"E": ['~', '`', '$', "£"],
"O": ['+', '-', '_', ")"]}
reverse_vowel_map = {}
for vowels, symbols in vowel_map.items():
 for symbol in symbols:
  reverse_vowel_map[symbol] = vowels

while True:
    pilihan = input("Encrypt / Decrypt (E/D): ").upper()

    if pilihan == "E":
        text = input("Masukkan teks: ")
        while True:
            try:
                shift = int(input("Masukkan shift: "))
                if shift >= 0:
                 break
                else:
                 print("Shift tidak boleh negatif.")
            except ValueError:
                print("Masukkan angka yang valid.")
        for char in text:
            if char.isalpha():

                if char.upper() in vowel_map:
                  index = (position - 1) % 4
                  encrypted = vowel_map[char.upper()][index]
                  if char.isupper():
                     print("^", end="")
                  print(encrypted, end="")
                else:
                 if char.isupper():
                    encrypted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                 else:
                    encrypted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                 print(encrypted, end="")
                position += 1
                
            else: print(char, end="")
        print()
        break

    elif pilihan == "D":
        teks = input("Masukkan teks: ")
        while True:
                    try:
                        shift = int(input("Masukkan shift: "))
                        if shift >= 0:
                         break
                        else:
                         print("Shift tidak boleh negatif.")
                    except ValueError:
                        print("Masukkan angka yang valid.")
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
                    decrypted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                else:
                    decrypted = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
           else:
                decrypted = char
           print(decrypted, end="")
        print()
        break

    else:
        print("Dumbass")
