# -*- coding: utf-8 -*-
"""5210411216_RESTIAN DWI FRIWALDI

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zDa9aqJD7eYSif4RI_aeRM796shFewQB
"""

from datetime import date
class InvalidInputError(Exception):
    pass

def hitung_total_harga(harga_permalam, lama_hari):
    return harga_permalam * lama_hari

def pesan_kamar_hotel():
    print("=" * 50)
    print("        Selamat Datang di M Hotel!")
    print("=" * 50)
    while True:
        try:
            nama_pemesan = input("Masukkan nama Anda: ")
            break
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh pengguna.")
            return

    print("Jenis Kamar:")
    print("1. Standard   (Rp. 100000/malam)")
    print("2. Suite      (Rp. 200000/malam)")
    print("3. Deluxe     (Rp. 500000/malam)")
    print("4. Executive  (Rp. 1000000/malam)")

    while True:
        try:
            jenis_kamar = input("Pilih Jenis Kamar Yang Akan Dipesan (1/2/3/4): ")
            if jenis_kamar not in ['1', '2', '3', '4']:
                raise InvalidInputError("Jenis kamar yang dipilih tidak valid.")
            break
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh pengguna.")
            return
        except InvalidInputError as e:
            print("Error:", str(e))

    while True:
        try:
            lama_hari = input("Masukkan Jumlah Hari Pemesanan: ")
            if not lama_hari.isdigit():
                raise InvalidInputError("Jumlah hari pemesanan harus berupa angka.")
            lama_hari = int(lama_hari)
            break
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh pengguna.")
            return
        except InvalidInputError as e:
            print("Error:", str(e))

    if jenis_kamar == '1':
        nama_kamar = "Standard"
        harga_permalam = 100000
        jumlah_kamar = 10
    elif jenis_kamar == '2':
        nama_kamar = "Suite"
        harga_permalam = 200000
        jumlah_kamar = 5
    elif jenis_kamar == '3':
        nama_kamar = "Deluxe"
        harga_permalam = 500000
        jumlah_kamar = 3
    else:
        nama_kamar = "Executive"
        harga_permalam = 1000000
        jumlah_kamar = 2

    if jumlah_kamar == 0:
        print("Kamar yang dipilih tidak tersedia.")
        return

    total_harga = hitung_total_harga(harga_permalam, lama_hari)
    nomor_kamar = str(jumlah_kamar)
    tanggal_pesanan = date.today().strftime("%d-%m-%Y")

    print("\n" + "=" * 16 + " Detail Pemesanan " + "=" * 16)
    print("Nama Pemesan    : ", nama_pemesan)
    print("Jenis Kamar     : ", nama_kamar)
    print("Nomor Kamar     : ", nomor_kamar)
    print("Lama Menginap   : ", lama_hari, "hari")
    print("Tanggal Pesanan : ", tanggal_pesanan)
    print("Total Harga     :  Rp.", total_harga)
    print("=" * 50)

pesan_kamar_hotel()