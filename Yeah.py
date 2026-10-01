while True:
    pilihan = input("Encrypt / Decrypt (E/D): ").upper()

    if pilihan == "E":
        text = input("Masukkan teks: ")

        vowels = "AIUEO"
        shift = 5
        position = 1
        vowel_map = {
        "A": ['#', '*', '"', "!"],
        "I": ['>', '/', '.', "@"],
        "U": ['<', '[', '&', "%"],
        "E": ['~', '`', '$', "^"],
        "O": ['+', '-', '_', "~"]}

        for char in text:
            if char.isalpha():

                if char.upper() in vowel_map:
                  index = (position - 1) % 4
                  encrypted = vowel_map[char.upper()][index]
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
        print("Ntar dulu")
        break

    else:
        print("Dumbass")
