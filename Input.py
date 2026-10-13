from EnD import encrypt, decrypt

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