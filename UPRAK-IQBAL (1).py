print("1. Balok")

panjang = int(input("masukkan nilai panjang"))
lebar = int(input("masukkan nilai lebar"))
tinggi = int(input("masukkan nilai tinggi"))

volume_bal = panjang * lebar * tinggi
print("Nilai volume balok adalah", volume_bal)

print("\n2. Tabung")

luas_alas_lingkaran = int(input("masukkan nilai luas alas lingkaran"))
tinggi = int(input("masukkan nilai tinggi"))

volume_ling = luas_alas_lingkaran * tinggi
print("nilai volume tabung adalah", volume_ling)

print("\n3. Limas")

Luas_alas_persegi = int(input("masukkan nilai Luas alas persegi"))
tinggi = int(input("masukkan nilai tinggi"))
volume_lim = (1/3 * Luas_alas_persegi) * tinggi

print("\n4. konversi dollar")

x = int(input("Masukkan nilai dollar"))
y = x * 14000
print(x, "dollar =", y, "rupiah")
