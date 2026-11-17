# TUPLE: Identitas mesin (statis)
INFO_SERVER = ("SRV-AI_CORE", -7.7956, 110.3695)

def kalkulasi_statistik(data_list):
    """Menghitung statistik dari list suhu."""
    if len(data_list) == 0:
        return 0, 0, 0

    rata_rata = sum(data_list) / len(data_list)
    return rata_rata, max(data_list), min(data_list)

def evaluasi_kondisi(rata_rata):
    """menentukan status keamanan."""
    if rata_rata >= 120.0:
        return "[BAHAYA] Server Overheating! Matikan Sistem!"
    elif rata_rata >= 80.0:
        return "[WASPADA] SUhu Tinggi. Nyalakan kipas tambahan."
    else:
        return "[AMAN] Suhu Server Stabil."