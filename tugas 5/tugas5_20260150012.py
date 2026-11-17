import modul_konversi
 
GARIS = "=" * 48
 
 
def main():
    print(GARIS)
    print("ANALISIS KONSUMSI DAYA PERANGKAT EDGE AI".center(48))
    print(GARIS)
 
    # INPUT dari pengguna
    nama = input("Masukkan Nama Perangkat AI : ")
    voltase = float(input("Masukkan Voltase (Volt)    : ").replace(",", "."))
    arus = float(input("Masukkan Arus (Ampere)     : ").replace(",", "."))
 
    # Memanggil fungsi dari modul
    daya = modul_konversi.hitung_daya(voltase, arus)
    kategori = modul_konversi.kategori_konsumsi(daya)
 
    # OUTPUT rangkuman hasil
    print()
    print(GARIS)
    print("HASIL ANALISIS".center(48))
    print(GARIS)
    print(f"Nama Perangkat   : {nama}")
    print(f"Voltase          : {voltase} Volt")
    print(f"Arus             : {arus} Ampere")
    print(f"Daya             : {daya:.2f} Watt")
    print(f"Kategori Konsumsi: {kategori}")
    print(GARIS)
 
 
if __name__ == "__main__":
    main()