def harga_tiket(umur):
    if umur <= 2:
        return 0
    elif 3 <= umur <= 12:
        return 14
    elif umur >= 65:
        return 18
    else:
        return 23


total = 0

while True:
    umur = input("masukkan umur: ").strip()

    # input kosong = selesai
    if umur == "":
        break

    harga = harga_tiket(int(umur))

    if harga == 0:
        print("Gratis")
    else:
        print(f"Harga ${harga:.2f}")

    total += harga
    print(f"Running total: {total:.2f}")

# pembayaran
while True:
    uang = float(input("masukkan jumlah uang: "))

    if uang >= total:
        print(f"Running kembalian: {uang - total:.2f}")
        break
    else:
        print(f"Uang kurang ${total - uang:.2f}, silakan masukkan lagi")
