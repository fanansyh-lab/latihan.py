#program perhitungan diskon belanja

Total = int(input("Masukkan total belanja:"))
Member = input("Apakah member (y/n): ").lower()

# Tentukan diskon berdasarkan total belanja
if Total >= 500000:
    Diskon = 20
elif Total >= 300000:
    Diskon = 15
elif Total >= 100000:
    Diskon = 10
else:
    Diskon = 0

    # Tambahan diskon untuk member
if Member == "y":
    Diskon += 10

potongan = Total * Diskon / 100
bayar = Total - potongan

print()
print(f"Total belanja : Rp{Total:,}".replace(",", "."))
print(f"Diskon        : {Diskon}%")
print(f"Potongan      : Rp{int(potongan):,}".replace(",", "."))
print(f"Total bayar   : Rp{int(bayar):,}".replace(",", "."))