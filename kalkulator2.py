class kalkulator:
    def __init__(self):
        self.hasil = 0

    def kalkulator(self, operation, x, y):
        if operation == '+':
            return x + y
        if operation == '-':
            return x - y
        if operation == '*':
            return x * y 
        if operation == '/':
            return "Error: Tidak bisa membagi dengan nol!" if y == 0 else x / y
        else:
            return "Operasi tidak valid!"
        
    def run(self):
        print("\n========= Kalkulator Sederhana =========")
        while True:
            print("\nPilih operator: +, -, *, /")
            operation = input("Masukan operasi atau 'NO' untuk keluar: ")

            if operation == 'NO':
                print("Terimakasih telah menggunakan kalkulator!")
                break

            try:
                num1 = float(input("Masukan angka pertama: "))
                num2 = float(input("Masukan ini angka kedua: "))
                result = self.kalkulator(operation, num1, num2)
                print(f"Hasil: {result}")
            except ValueError:
                print("Error: Masukan angka yang valid!")

if __name__ == "__main__":
    calc = kalkulator()
    calc.run()