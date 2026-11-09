#065002600012
#Centrino Wahyu Alli Raid
def jumlahkan(n, ke=1):
    if ke > n:                     
        return 0
    angka = int(input(f"Masukkan bilangan ke-{ke}: "))
    return angka + jumlahkan(n, ke + 1)  


jumlah = int(input("Masukkan Jumlah: "))
hasil = jumlahkan(jumlah)
print("Hasil dari penjumlahan adalah:", hasil)
