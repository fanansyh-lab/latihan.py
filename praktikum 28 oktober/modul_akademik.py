def hitung_rata_rata(nilai_tugas, nilai_uts, nilai_uas):
    """Fungsi ini meghitung rata-rata dari 3 komponen nilai."""
    total = nilai_tugas + nilai_uts + nilai_uas
    rata_rata = total / 3
    return rata_rata

def tentukan_status_kelulusan(rata_rata):
    """Fungsi ini menentukan status kelulusan berdasarkan rata-rata nilai."""
    if rata_rata >= 80:
        return "A (Lulus Sangat Baik)"
    elif rata_rata >= 70:
        return "B (Lulus Baik)"
    elif rata_rata >= 60:
        return "C (Lulus Cukup)"
    elif rata_rata >= 50:
        return "D (Tidak Lulus - mengulang)"
    else:
        return "E (Tidak Lulus - mengulang)"