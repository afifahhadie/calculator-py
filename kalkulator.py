def initambah(x, y):
    return x + y

def inikurang(x, y):
    return x - y

def inikali(x, y):
    return x * y

def inibagi(x, y):
    if y == 0:
        return "Error: Tidak bisa membagi dengan nol!"
    return x / y

print("======== Kalkulator Sederhana ========")
print("Pilih operasi: ")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

while True:
    pilih = input("Masukan pilihan (1/2/3/4) atau 'q' untuk keluar: ")

    if pilih == 'q':
        print("Terimakasih telah menggunakan kalkulatro ini!")
        break

    if pilih in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Masukan angka pertama: "))
            num2 = float(input("Masukan angka kedua: "))

            if pilih == '1':
                print(f"Hasil: {num1} + {num2} = {initambah(num1, num2)}")
            elif pilih == '2':
                print(f"Hasil {num1} - {num2} = {inikurang(num1, num2)}")
            elif pilih == '3':
                print(f"Hasil : {num1} * {num2} = {inikali(num1, num2)}")
            elif pilih == '4':
                print(f"Hasil: {num1} / {num2} = {inibagi(num1, num2)}")
        except ValueError:
            print("Error: masukkan angka yang valid!")
    else:
        print("Pilihan tidak valid, coba lagi!")