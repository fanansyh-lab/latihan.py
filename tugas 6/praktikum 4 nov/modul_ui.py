import modul_sistem

def input_suhu_valid():
    """Fungsi spesifik untuk mencegat error (Debugging)"""
    while True:
        try:
            suhu = float(input("masukkan data suhu terbaru (celcius): "))
            if suhu < 0 or suhu > 150:
                print(" -> [WARNING] Suhu Tidak Rasional (0-150 C)!\n")
                continue
            return suhu
        except ValueError:
            print(" -> [ERROR] Format Salah! Harap masukkan ANGKA.\n")

def jalankan_aplikasi():
    """Fungsi raksasa yang membungkus seluruh menu (Controller)"""
    
    # LIST: Disimpan disini karena ini data operasional yang berubah-ubah
    # log_suhu_server = []
     
# Memanggil data tuple dari modul_sistem.py
nama, lat, lon = modul_sistem.INFO_SERVER

print("============================================")
print(f" SISTEM PEMANTAUAN: {nama} ({lat}, {lon})")
print("============================================")

log_suhu_server = []

while True:
        print("\n--- Menu UTAMA ---")
        print("1. Tambah Data Suhu")
        print("2. Lihat Laporan Analisis")
        print("3. Hapus Data Terakhir")
        print("4. Keluar Sistem")

        try:
            pilihan = int(input("Pilih menu (1-4): "))

            if pilihan == 1:
                suhu_baru = input_suhu_valid()
                log_suhu_server.append(suhu_baru)
                print(f" -> Suhu {suhu_baru} C ditambahkan.")

            elif pilihan == 2:
                if len(log_suhu_server) == 0:
                    print(" -> Belum ada data direkam.")
                    continue

                # penerapan slicing untuk menampilkan 3 data terakhir
                tiga_terbaru = log_suhu_server[-3:] # slicing dari indeks -3 sampai akhir
                print(f"\n[INFO SLICING] 3 Suhu Terakhir: {tiga_terbaru}")

                # Penenrapan slicing untuk menampilkan data terbalik
                data_terbalik = log_suhu_server[::-1]

                print("\nRiwayat Suhu (Diurutkan dari yang paling baru):")

                for i, suhu in enumerate(data_terbalik, start=1):
                    print(f" Data ke - {len(log_suhu_server) - i}: {suhu} C")

                # Melempar list ke modul sistem untuk di hitung
                rata, max_s, min_s = modul_sistem.kalkulasi_statistik(log_suhu_server)
                status = modul_sistem.evaluasi_kondisi(rata)

                print(f"\nRata-rata: {rata:.2f} C | Max: {max_s} C | Min: {min_s} C")
                print(f"Status: {status}")
            elif pilihan == 3:
                if log_suhu_server:
                    print(f" -> Data ({log_suhu_server[-1]} C) dihapus.")
                else:
                    print(" -> Riwayat kosong!.")

           
            elif pilihan == 4:
                print("\nSistem dimatikan.")
                break
            else:
                print("[WARNING] Pilih 1, 2, 3, atau 4.")

        except ValueError:
            print("[ERROR SYSTEM] Harap masukkan angka menu.\n")    