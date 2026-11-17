def hitung_nilai_akhir(tugas, ucp1, ucp2):
    # bobot: tugas 20%, ucp1 40%, ucp2 40%
    nilai_akhir = (tugas * 0.20) + (ucp1 * 0.40) + (ucp2 * 0.40)
    return nilai_akhir

def tentukan_grade(nilai):
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"