def get_ordinal(n):
    """
    Fungsi untuk menentukan akhiran ordinal ('st', 'nd', 'rd', 'th') 
    berdasarkan angka yang dimasukkan.
    """
    if 11 <= n % 100 <= 13:
        suffix = 'th'
    else:
        last_digit = n % 10
        if last_digit == 1:
            suffix = 'st'
        elif last_digit == 2:
            suffix = 'nd'
        elif last_digit == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
    
    return (n, suffix)

def main():
    print("Ordinal Number")
    print("ketik 0 untuk menghentikan program")
    
    while True:
        try:
            angka = int(input("masukkan angka: "))
            hasil = get_ordinal(angka)
            print(hasil)
            
            if angka == 0:
                print("terima kasih telah menggunakan program saya")
                break
        except ValueError:
            print("Masukkan angka bulat yang valid!")

if __name__ == "__main__":
    main()
