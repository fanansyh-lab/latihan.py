# TUGAS 2 PRAKTIKUM PEMDAS
# Nama : Faruq Adi Fanansyah
# NIM  : 20260150012

print("--- INPUT DATA DIRI & BMI ---")
nama = input("Nama mahasiswa: ") or "Faruq Adi Fanansyah"
nim = input("NIM: ") or "20260150012"

input_bb = input("Berat badan (kg): ")
bb = float(input_bb) if input_bb else 80.0

input_tb = input("Tinggi badan (cm): ")
tb_cm = float(input_tb) if input_tb else 168.0

# Hitung BMI
tb_m = tb_cm / 100
bmi = bb / (tb_m ** 2)



print("\n--- INPUT BELANJAAN KASIR ---")
barang1 = input("Nama barang pertama : Kopi ") 
input_h1 = input("Harga barang pertama: Rp15000 ")
harga1 = float(input_h1) if input_h1 else 15000.0

barang2 = input("Nama barang kedua   :beras ")
input_h2 = input("Harga barang kedua  : Rp23000 ")
harga2 = float(input_h2) if input_h2 else 23000.0

# Hitung-hitungan kasir
subtotal = harga1 + harga2
diskon = subtotal * 0.05
setelah_diskon = subtotal - diskon
pajak = setelah_diskon * 0.11
total_akhir = setelah_diskon + pajak

# Menampilkan hasil
print("\n" + "="*35)
print("          HASIL PERHITUNGAN        ")
print("="*35)
print("Nama        :", nama)
print("NIM         :", nim)
print("BMI Anda    :", round(bmi, 2))
print("-----------------------------------")
print("Barang 1    :", barang1, "- Rp", harga1)
print("Barang 2    :", barang2, "- Rp", harga2)
print("-----------------------------------")
print("Subtotal    : Rp", round(subtotal, 2))
print("Diskon (5%) : Rp", round(diskon, 2))
print("Pajak (11%) : Rp", round(pajak, 2))
print("TOTAL BAYAR : Rp", round(total_akhir, 2))
print("="*35)