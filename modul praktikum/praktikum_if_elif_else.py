print("="*50)
print("--- PRAKTIKUM 3:IF, ELIF, DAN ELSE ---")
print("="*50)

#----------------------------------------------
print("\n--- LATIHAN 3: PENDEKATAN IF-ELIF-ELSE ---")
print("{|} Mengecek grade nilai DENGAN menggunakan ELIF")
nilai = float(input("masukkan nilai akhir Anda (0-100): "))

# memanfaatkan variabel 'nilai' dari input Latihan 2
if nilai >= 80:
    print("Evaluasi IF-ELIF-ELSE: Grade A (Lulus)")
elif nilai >= 70:
    print("Evaluasi IF-ELIF-ELSE: Grade B (Lulus)")
elif nilai >= 60:
    print("Evaluasi IF-ELIF-ELSE: Grade C (Lulus)")
elif nilai >= 50:
    print("Evaluasi IF-ELIF-ELSE: Grade D (Tidak Lulus)")
else:
    print("Evaluasi IF-ELIF-ELSE: Grade E (Tidak Lulus)")