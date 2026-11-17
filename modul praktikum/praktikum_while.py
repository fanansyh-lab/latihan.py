print("n===============================")
print("          BAGIAN 2: WHILE LOOP      ")
print("===============================")

print("a. Menghitung menggunakan while (dengan jeda):")
hitung = 1
while hitung <= 3:
    print("hitungan while ke-", hitung)
    hitung = hitung + 1

print("\nb. Program interaktif dengan user:")
kata_kunci = ""

while kata_kunci != "berhenti":
    kata_kunci = input("ketik kata 'berhenti' untuk keluar dari program: ")

    if kata_kunci != "berhenti":
        print("-> memeriksa input...")
        print("-> anda mengetik:", kata_kunci, "program masih berulang!\n")

print("\nMemproses jalan keluar...")
print("Selamat! anda berhasil keluar dari perulangan while.:")