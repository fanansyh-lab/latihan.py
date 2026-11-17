#-------------------------------------------------------------
print("\n--- LATIHAN 4: NESTED IF & OPERATOR LOGIKA ---")
print("{|} Simulasi Penentuan Predikat Kelulusan Cumlaude")

ipk = float(input("Masukkan IPK Anda (0.0-4.0): "))
masa_studi = int(input("Masukkan masa studi Anda (dalam semester): "))

# menggunakan operator 'and' (kedua syarat harus true)
if ipk >= 3.51 and masa_studi <= 8:
    print("-> Syarat dasar cumlaude terpenuhi.")

    #Nested IF (Pengecekan lamjutan di dalam blok true)
    nilai_d = input("Apakah Anda memiliki nilai D? (ya/tidak): ")
    if nilai_d == "tidak":
        print("SSTATUS AKHIR: LULUS DENGAN PUJIAN (CUMLAUDE).")
    else:
        print("STATUS AKHIR: LULUS SANGAT MEMUASKAN (gagal cumlaude karena nilai D).")

else:
    print("STATUS AKHIR: LULUS BIASA (Tidak memenuhi standar IPK/Masa Studi)")

print("\n" + "="*50)