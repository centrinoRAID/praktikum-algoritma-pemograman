def pangkat_rekursif(base, power):
    if power == 0:
        return 1
    elif power < 0:
        return 1 / pangkat_rekursif(base, -power)
    else:
        return base * pangkat_rekursif(base, power - 1)


def main():
    print(
        "Ini merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti"
    )

    while True:
        input_angka = input("Masukkan Angka: ")
        if input_angka.strip() == "":
            print("Program Selesai")
            break

        try:
            angka = float(input_angka)
            pangkat = float(input("Masukkan Pangkatnya: "))
            hasil = pangkat_rekursif(angka, pangkat)
            if hasil.is_integer():
                hasil = int(hasil)

            print(f"Hasilnya adalah: {hasil}\n")
        except ValueError:
            print("Input harus berupa angka! Silakan coba lagi.\n")


if __name__ == "__main__":
    main()
