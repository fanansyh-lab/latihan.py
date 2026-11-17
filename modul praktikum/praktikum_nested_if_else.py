print("="*50)
print("--- PRAKTIKUM 3:IF, ELIF, DAN ELSE ---")
print("="*50)

#----------------------------------------------
print("\n--- LATIHAN 2: PENDEKATAN NESTED IF-ELSE ---")
print("{|} Mengecek grade nilai TANPA menggunakan ELIF")
nilai = float(input("masukkan nilai akhir Anda (0-100): "))

if nilai >= 80:
    print("Evaluasi Nested: Grade A (Lulus)")
else:
    if nilai >= 70:
        print("Evaluasi Nested: Grade B (Lulus)")
    else:
        if nilai >= 60:
            print("Evaluasi Nested: Grade C (Lulus)")
        else:
            if nilai >= 50:
                print("Evaluasi Nested: Grade D (Tidak Lulus)")
            else:
                print("Evaluasi Nested: Grade E (Tidak Lulus)")