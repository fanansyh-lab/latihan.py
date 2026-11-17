# 1. MODULARISASI: Memanggil file modul_akademik.py
import modul_akademik
import modul_input

#==========================================================
# BLOK ANTARMUKA PENGGUNA (MAIN INTERFACE)
#==========================================================
print("==============================================")
print("        SISTEM AKADEMIK: INPUT NILAI MAHASISWA")
print("==============================================")

nama_mhs = input("Masukkan nama mahasiswa: ")

print("\n--- Mulai Proses Input Nilai ---")
# memanggil fungsi validasi berulang kali untuk setiap nilai
nilai_tugas = modul_input.minta_input_nilai("Tugas")
nilai_uts = modul_input.minta_input_nilai("UTS")    
nilai_uas = modul_input.minta_input_nilai("UAS")

print ("\n--- Sedang Memproses Data... ---")

# menggunakan fungsi dari modul terpisah (modul_akademik)
nilai_akhir = modul_akademik.hitung_rata_rata(nilai_tugas, nilai_uts, nilai_uas)
status_akhir = modul_akademik.tentukan_status_kelulusan(nilai_akhir)

# Menampilkan hasil akhir
print("===============================================")
print(f" HASIL EVALUASI: {nama_mhs.upper() }")
print("===============================================")
print(f" Nilai Rata-rata: {nilai_akhir:.2f}")
print(f"Status & Grade : {status_akhir}")
print("===============================================")