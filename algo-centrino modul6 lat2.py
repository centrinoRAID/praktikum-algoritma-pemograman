def kabisat(tahun):
    """Mengembalikan True jika tahun kabisat, False jika bukan."""
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

def jumlah_hari(bulan, tahun=None):
    """Mengembalikan jumlah hari dalam bulan. Tahun hanya dipakai untuk Februari."""
    if bulan == 2:
        if kabisat(tahun):
            return 29
        return 28
    elif bulan in (4, 6, 9, 11):
        return 30
    else:
        return 31

print("Program ini akan menentukan jumlah hari dalam bulan tertentu")

while True:
    print("Masukkan 0 untuk menghentikan program")
    bulan = int(input("masukkan bulan (1-12): "))

    if bulan == 0:
        print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.")
        break

    if bulan < 1 or bulan > 12:
        print("Bulan tidak valid, masukkan angka 1 sampai 12")
        continue

    if bulan == 2:
        tahun = int(input("masukkan tahun (misalnya 2021): "))
        hari = jumlah_hari(bulan, tahun)
    else:
        hari = jumlah_hari(bulan)

    print(hari, "hari dalam sebulan")
