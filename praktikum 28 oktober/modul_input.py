def minta_input_nilai(nama_komponen):
    """
    fungsi ini akan terus mengulang (while) meminta input
    sampai user memasukkan ANGKA yang VALID (0-100).
    """
    while True:
        try:
            # Mencoba menerima input dan mengubahnya ke desimal (float)
            teks_input = input(f"Masukkan nilai {nama_komponen} (0-100): ")
            nilai = float(teks_input)

            # debugging logika: Mencegah nilai minus atau lebih dari 100
            if nilai < 0 or nilai > 100:
                print("[WARING] Nilai tidak masuk akal! Harap masukkan rentang 0 hingga 100.\n.")
                continue # Mengulang loop kembali ke atas

            # jika semua aman, kembalikan nilai dan hentikan loop
            return nilai

        except ValueError:
            # menangkap error jika user memasukkan huruf (misal: "delapan puluh")
            print("[ERROR SYSTEM] Tipe data salah! Anda memasukkan teks, harap masukkan ANGKA.\n")