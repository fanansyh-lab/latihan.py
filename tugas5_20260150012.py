# Tugas Praktikum 5 - Pemrograman Dasar (AI104)
# Nama : Faruq Adi Fanansyah
# NIM  : 20260150012
# Topik: Struktur Perulangan (while dan for)

# =====================================================
# BAGIAN 1 : Sistem Keamanan Login (pakai while)
# =====================================================
sandi_rahasia = "AI2026"
percobaan = 0
akses = False

while percobaan < 3:
    sandi = input("Masukkan password: ")
    percobaan = percobaan + 1

    if sandi == sandi_rahasia:
        akses = True
        break  # password benar, keluar dari while
    else:
        print("Password salah! Sisa percobaan:", 3 - percobaan)

# cek hasil login
if akses == False:
    print("Sistem Terkunci!")
    exit()  # program berhenti kalau gagal 3 kali

print("Akses Diberikan!")
print()

# =====================================================
# BAGIAN 2 : Analisis Suhu Server (pakai for)
# =====================================================
total_suhu = 0
suhu_tertinggi = 0

print("=== Input Suhu Server 5 Hari ===")
for hari in range(1, 6):
    suhu = float(input("Masukkan suhu server hari ke-" + str(hari) + ": "))
    total_suhu = total_suhu + suhu

    # cari suhu tertinggi
    if suhu > suhu_tertinggi:
        suhu_tertinggi = suhu

rata_rata = total_suhu / 5

print()
print("=== Rekapitulasi Suhu Server ===")
print("Total Suhu     :", total_suhu)
print("Rata-rata Suhu :", rata_rata)
print("Suhu Tertinggi :", suhu_tertinggi)