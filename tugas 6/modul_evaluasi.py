def hitung_persentase_presensi(hadir, total_pertemuan=14):
    """Menghitung persentase kehadiran berdasarkan jumlah hadir dan total pertemuan."""
    return (hadir / total_pertemuan) * 100


def hitung_nilai_akhir(tugas, ucp1, ucp2):
    """Menghitung Nilai Akhir dengan bobot: Tugas (20%), UCP 1 (40%), UCP 2 (40%)."""
    nilai_akhir = (tugas * 0.20) + (ucp1 * 0.40) + (ucp2 * 0.40)
    return nilai_akhir


def cek_kelayakan_aslab(persentase_presensi, nilai_akhir):
    """Menentukan status kelayakan asisten laboratorium berdasarkan presensi dan nilai akhir."""
    if persentase_presensi < 75.0:
        return "DITOLAK (Kehadiran di bawah 75%)"
    elif persentase_presensi >= 75.0 and nilai_akhir >= 75.0:
        return "DITERIMA (Memenuhi Syarat)"
    else:  # persentase_presensi >= 75.0 TETAPI nilai_akhir < 75.0
        return "DITOLAK (Nilai Akhir Kurang)"