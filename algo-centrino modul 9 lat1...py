def tulis_file(nama, umur, alamat, email, dosen_wali):
    file = open("Biodata.txt", "w")
    file.write("Nama: " + nama + "\n")
    file.write("Umur: " + umur + "\n")
    file.write("Alamat: " + alamat + "\n")
    file.write("Email: " + email + "\n")
    file.write("Dosen Wali: " + dosen_wali + "\n")
    file.close()


def baca_file():
    file = open("Biodata.txt", "r") 
    isi = file.read()
    file.close()
    return isi


nama = input("Masukkan Nama mu: ")
umur = input("Masukkan Umur mu: ")
alamat = input("Masukkan Alamatmu: ")
email = input("Masukkan Emailmu: ")
dosen_wali = input("Masukkan Dosen Walimu: ")

tulis_file(nama, umur, alamat, email, dosen_wali)
print()
print("Berikut Ini Data Kamu")
print(baca_file())
