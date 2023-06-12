# Membuat Program Menggunakan if else elif, operator Math, dan list
import math
operasiMath = input("Perhitungan Luas Bangun : ")


def perhitunganMath(namaBangun):
    match namaBangun:
        case "Persegi Panjang":
            print(f"Luas bangun {operasiMath}")

            angka = int(input("Panjang : "))
            angka2 = int(input("Lebar : "))

            hasil = angka * angka2
            print(f"{angka} x {angka2} = {hasil}")

        case "Persegi":
            print(f"Luas bangun {operasiMath}")

            angka = int(input("Sisi : "))

            hasil = angka ** 2
            print(f"{angka}^2 = {hasil}")

        case "Lingkaran":
            print(f"Luas bangun {operasiMath}")

            angka = int(input("Jari-jari : "))

            hasil = math.pi * (angka**2)
            print(f"phi x {angka}^2 = {hasil}")

        case "Segitiga":
            print(f"Luas bangun {operasiMath}")

            angka = int(input("Alas : "))
            angka2 = int(input("Tinggi : "))

            hasil = int(1/2 * angka * angka2)
            print(f"1/2 x {angka} x {angka2} = {hasil}")

        case default:
            print(f"Operasi perhitungan {operasiMath} MBOTEN WONTEN HEHE")


perhitunganMath(operasiMath)
