#065002600012
#Centrin oWahyu Alli Raid
def cek_prima(angka):
    if angka < 2:
        return False
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True


def tampilkan_hasil(angka):
    if cek_prima(angka):
        print(f"{angka} adalah bilangan Prima")
    else:
        print(f"{angka} bukanlah bilangan Prima")


ulang = "y"
while ulang.lower() == "y":
    angka = int(input("Masukkan angka: "))
    tampilkan_hasil(angka)
    ulang = input("Coba angka lain? (y/n): ")

print("Program selesai.")
