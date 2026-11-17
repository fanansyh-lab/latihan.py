def hitung_daya(voltase, arus):
    """Menghitung daya listrik dalam Watt.
 
    Rumus: Daya = Voltase x Arus
    """
    return voltase * arus
 
 
def kategori_konsumsi(daya):
    """Mengembalikan kategori konsumsi berdasarkan daya (Watt)."""
    if daya < 10:
        return "Hemat (Low Power)"
    elif daya <= 50:
        return "Normal"
    else:
        return "Tinggi (High Power - Perlu Heatsink)"