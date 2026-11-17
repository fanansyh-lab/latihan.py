# mengimpor modul buatan sendiri
import modul_skoring

print("================================")
print("   sistem input nilai akhir ai  ")
print("================================")

# 1. proses input
nama_mk = "Pemograman Dasar AI"
in_tugas = float(input("Masukkan nilai tugas mandiri (1-100) : "))
in_ucp1 = float(input("Masukkan nilai UCP 1 (1-100) : "))
in_ucp2 = float(input("Masukkan nilai UCP 2 (1-100) : "))

# 2. Proses Pemanggilan Fungsi Modul
nilai_akhir = modul_skoring.hitung_nilai_akhir(in_tugas, in_ucp1, in_ucp2)
grade = modul_skoring.tentukan_grade(nilai_akhir)

# 3. Proses Output
print("\n================================")
print(f"RANGKUMAN NILAI: {nama_mk}")
print("================================")
print(f"Nilai Akhir (kalkulasi) : {nilai_akhir:.2f}")
print(f"Grade Mutu              : {grade}")
print("================================")