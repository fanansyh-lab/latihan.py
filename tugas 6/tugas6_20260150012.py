# Impor dari modul_evaluasi
import modul_evaluasi


def input_angka_valid(prompt, min_val, max_val):
    """Fungsi validasi anti-crash untuk memastikan input berupa angka dan dalam rentang tertentu."""
    while True:
        try:
            nilai = float(input(prompt))
            if nilai < min_val or nilai > max_val:
                print(
                    f"[WARNING] Nilai harus berada di antara {min_val} hingga {max_val}. Silakan coba lagi."
                )
            else:
                return nilai
        except ValueError:
            print("[ERROR] Masukan tidak valid! Harap masukkan angka yang benar.")


def main():
    while True:
        print("\n--- SISTEM EVALUASI KELAYAKAN ASLAB AI ---")
        print("1. Hitung Kelayakan")
        print("2. Keluar")

        try:
            pilihan = int(input("Pilih menu (1/2): "))
        except ValueError:
            print(
                "[ERROR] Pilihan menu tidak valid! Harap masukkan angka 1 atau 2."
            )
            continue

        if pilihan == 1:
            # Input Data Diri
            nama = input("Masukkan Nama Lengkap: ")
            nim = input("Masukkan NIM: ")

            print("\n--- Masukkan Komponen Penilaian ---")
            # Validasi kehadiran (0 - 14)
            jumlah_hadir = input_angka_valid(
                "Jumlah Kehadiran (0-14): ", 0, 14
            )
            # Validasi nilai Tugas, UCP 1, UCP 2 (0 - 100)
            nilai_tugas = input_angka_valid("Nilai Tugas (0-100): ", 0, 100)
            nilai_ucp1 = input_angka_valid("Nilai UCP 1 (0-100): ", 0, 100)
            nilai_ucp2 = input_angka_valid("Nilai UCP 2 (0-100): ", 0, 100)

            # Proses Perhitungan menggunakan fungsi dari modul
            persentase = modul_evaluasi.hitung_persentase_presensi(jumlah_hadir)
            nilai_akhir = modul_evaluasi.hitung_nilai_akhir(
                nilai_tugas, nilai_ucp1, nilai_ucp2
            )
            status = modul_evaluasi.cek_kelayakan_aslab(persentase, nilai_akhir)

            # Tampilkan Hasil dengan rapi
            print("\n" + "=" * 40)
            print("       HASIL EVALUASI KELAYAKAN ASLAB")
            print("=" * 40)
            print(f"Nama           : {nama}")
            print(f"NIM            : {nim}")
            print(f"Kehadiran      : {jumlah_hadir}/14 ({persentase:.2f}%)")
            print(f"Nilai Akhir    : {nilai_akhir:.2f}")
            print(f"Status Seleksi : {status}")
            print("=" * 40)

        elif pilihan == 2:
            print(
                "Terima kasih telah menggunakan Sistem Evaluasi Kelayakan Aslab AI."
            )
            break
        else:
            print(
                "[WARNING] Pilihan tidak tersedia. Silakan pilih 1 atau 2."
            )


if __name__ == "__main__":
    main()