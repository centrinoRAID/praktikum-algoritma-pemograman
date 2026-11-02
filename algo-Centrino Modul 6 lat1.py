
SKALA_DEFAULT = {"A": 4, "B": 3, "C": 2, "D": 1, "E": 0}

def konversi_nilai(huruf, skala=SKALA_DEFAULT):
    """Mengubah huruf menjadi angka. Mengembalikan None jika huruf tidak ada di skala."""
    return skala.get(huruf.upper())

def hitung_rata_rata(daftar_nilai, desimal=1):
    """Menghitung rata-rata. Parameter desimal punya nilai default 1."""
    if len(daftar_nilai) == 0:
        return None
    return round(sum(daftar_nilai) / len(daftar_nilai), desimal)

daftar = []
while True:
    huruf = input("masukkan nilai: ")
    if huruf == "":              # input kosong = selesai
        break
    angka = konversi_nilai(huruf)
    if angka is None:
        print("nilai tidak valid")
    else:
        print("nilai =", angka)
        daftar.append(angka)

print("Rata-ratanya adalah: ", hitung_rata_rata(daftar))
