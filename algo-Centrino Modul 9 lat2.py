#065002600012
#CENTRINO Wahyu Alli Raid
def buat_file(nama_file):
    nama = input("Masukkan Namamu: ")
    nim = input("Masukkan NIM kamu: ")
    angkatan = input("Masukkan tahun angkatanmu: ")

    file = open(nama_file + ".txt", "w")
    file.write("Nama: " + nama + "\n")
    file.write("NIM: " + nim + "\n")
    file.write("Angkatan: " + angkatan + "\n")
    file.close()

    print("\n\nFile Berhasil Dibuat\n\n")


def baca_file(nama_file):
    try:
        file = open(nama_file + ".txt", "r")
        isi = file.read()
        file.close()
        print("\n")
        print(isi)
    except FileNotFoundError:
        print("\nFile tidak ditemukan\n")


def tambah_file(nama_file):
    try:
        sahabat = input("Masukkan Nama Sahabatmu: ")
        catatan = input("Masukkan Catatan Tambahan kamu: ")

        file = open(nama_file + ".txt", "a")
        file.write("Nama Sahabat: " + sahabat + "\n")
        file.write("Catatan: " + catatan + "\n")
        file.close()

        print("\n\nData Berhasil Ditambahkan\n\n")
    except FileNotFoundError:
        print("\nFile tidak ditemukan\n")


pilihan = 0
while pilihan != 4:
    print("===== Program File Handling =====")
    print("1. Membuat dan Menulis File")
    print("2. Membaca File")
    print("3. Menambahkan Text Pada File")
    print("4. Keluar Dari Program")
    print()
    pilihan = int(input("Masukkan Pilihan Berupa Angka (1/2/3/4): "))

    if pilihan == 1:
        nama_file = input("Masukkan Nama File: ")
        buat_file(nama_file)
    elif pilihan == 2:
        nama_file = input("Masukkan Nama File: ")
        baca_file(nama_file)
    elif pilihan == 3:
        nama_file = input("Masukkan Nama File: ")
        tambah_file(nama_file)
    elif pilihan == 4:
        print("Terima Kasih Sudah Menggunakan Program Saya")
    else:
        print("Pilihan tidak valid, coba lagi\n")
