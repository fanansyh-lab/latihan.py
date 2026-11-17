# ---------- Konstanta tarif dan surcharge ----------
TARIF_DEKAT = 7000  # Jarak < 50km (Rp/kg)
TARIF_SEDANG = 12000  # Jarak >= 50 - 100 km (Rp/kg)
TARIF_JAUH = 17000  # Jarak > 100 km (Rp/kg)
PERSEN_SURCHARGE_KILAT = 0.20  # Surcharge layanan Kilat (20%)


def format_rupiah(nilai):
    """Mengubah angka menjadi format rupiah, contoh: Rp 12.500"""
    return "Rp {:,.0f}".format(nilai).replace(",", ".")


# ---------- 1. Input data dari pengguna ----------
print("=" * 45)
print(" AI-EXPRESS - KALKULASI BIAYAYA PENGIRIMAN")
print("=" * 45)

nama_pengirim = input("Nama Pengirim:Faruq Adi Fanansyah ") or "Faruq Adi Fanansyah"
berat_kg = float(input("Berat Paket (kg):10 ") or 10)
jarak_km = float(input("Jarak Pengiriman (km):80 ") or 80)
jenis_layanan = input("Jenis Layanan (Reguler/Kilat):kilat ") or "kilat"

# ---------- 2. Tentukan tarif per kg berdasarkan jarak ----------
if jarak_km < 50:
    tarif_per_kg = TARIF_DEKAT
elif 50 <= jarak_km <= 100:
    tarif_per_kg = TARIF_SEDANG
else:
    tarif_per_kg = TARIF_JAUH

# ---------- 3. Hitung biaya dasar ----------
biaya_dasar = berat_kg * tarif_per_kg

# ---------- 4. Hitung biaya tambahan berdasarkan jenis layanan ----------
print(repr(jenis_layanan.strip().lower()))
if jenis_layanan.strip().lower() == "kilat":
    biaya_tambahan = biaya_dasar * PERSEN_SURCHARGE_KILAT
    nama_layanan = "Kilat"
else:
    biaya_tambahan = 0
    nama_layanan = "Reguler"

# ---------- 5. Hitung total akhir ----------
total_biaya = biaya_dasar + biaya_tambahan

# ---------- Cetak struk ----------
print()
print("=" * 45)
print("          STRUK PENGIRIMAN AI-EXPRESS")
print("=" * 45)
print(f"Nama Pengirim    : {nama_pengirim}")
print(f"Berat Paket      : {berat_kg} kg")
print(f"Jarak Pengiriman : {jarak_km} km")
print(f"Jenis Layanan    : {nama_layanan}")
print("-" * 45)
print(f"Tarif per kg     : {format_rupiah(tarif_per_kg)}")
print(f"Biaya Dasar      : {format_rupiah(biaya_dasar)}")
print(f"Biaya Tambahan   : {format_rupiah(biaya_tambahan)}")
print("-" * 45)
print(f"TOTAL BIAYA      : {format_rupiah(total_biaya)}")
print("=" * 45)
print("   Terima kasih telah menggunakan layanan AI-EXPRESS!")
print("=" * 45)