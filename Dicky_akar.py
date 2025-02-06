# Program : Mencari akar suatu bilngan
# Programmer : Ahmad dicky priadi
# Tanggal Pembuatan : 6 february 2025

import math  # Mengimpor fungsi matematika 

# Meminta pengguna memasukkan angka
angka = float(input("Masukkan angka: "))

# Menghitung akar kuadrat
if angka >= 0:
    hasil = math.sqrt(angka)
    print(f"Akar kuadrat dari {angka} adalah {hasil}")
else:
    print("Tidak bisa menghitung akar kuadrat dari bilangan negatif!")
    