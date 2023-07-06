import os
import sys
os.system('cls')

class Data:
    def __init__(self, plat_nomor):
        self.plat_nomor = plat_nomor

class Parkiran:
    def __init__(self, kapasitas):
        self.kendaraan = []
        self.kapasitas = kapasitas

    def parkir_kendaraan(self, plat_nomor):
        if self.is_full():
            print('Parkiran penuh. Tidak dapat memasukkan kendaraan.')
        else:
            self.kendaraan.append(Data(plat_nomor))
            print(f"Kendaraan dengan plat nomor {plat_nomor} telah ditambahkan.")

    def keluarkan_kendaraan(self):
        if not self.is_empty():
            return self.kendaraan.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.kendaraan) == 0

    def is_full(self):
        return len(self.kendaraan) == self.kapasitas

    def size(self):
        return len(self.kendaraan)

    def tampilkan_kendaraan(self):
        print('Data Kendaraan di Parkiran'.center(50))
        print('+----+-------------+')
        print("| No | Plat Nomor  |")
        print('+----+-------------+')
        for i, s in enumerate(self.kendaraan):
            print(f"| {i+1:<2} | {s.plat_nomor:<12}| ")
            print('+----+-------------+')

    def urutkan_kendaraan(self):
        self.kendaraan.sort(key=lambda x: x.plat_nomor)

    def insert_kendaraan(self, plat_nomor, position):
        if self.is_full():
            print('Parkiran penuh. Tidak dapat memasukkan kendaraan.')
        elif position >= self.size():
            self.parkir_kendaraan(plat_nomor)
        else:
            self.kendaraan.insert(position, Data(plat_nomor))
            print(f"Kendaraan dengan plat nomor {plat_nomor} telah disisipkan pada posisi {position}.")

while True:
    kapasitas_parkiran1 = input("Masukkan kapasitas parkiran: ")
    
    if not kapasitas_parkiran1.isdigit():
        print("Inputan tidak valid. Harap masukkan angka.")
    elif int(kapasitas_parkiran1) == 0:
        print("Kapasitas parkiran tidak boleh nol.")
    else:
        kapasitas_parkiran = int(kapasitas_parkiran1)
        parkiran = Parkiran(kapasitas_parkiran)
        break

while True:
    print("Menu:")
    print("1. Parkir Kendaraan")
    print("2. Keluarkan Kendaraan")
    print("3. Tampilkan Kendaraan di Parkiran")
    print("4. Jumlah Kendaraan di Parkiran")
    print("5. Cek Parkiran Kosong")
    print("6. Cek Parkiran Penuh")
    print("7. Urutkan Kendaraan")
    print("8. Insert Kendaraan")
    print("9. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        plat_nomor = input("Masukkan Plat Nomor: ")
        parkiran.parkir_kendaraan(plat_nomor)
        
    elif pilihan == "2":
        kendaraan = parkiran.keluarkan_kendaraan()
        if kendaraan:
            print(f"Kendaraan dengan plat nomor {kendaraan.plat_nomor} telah dikeluarkan.")
        else:
            print("Tidak ada kendaraan dalam parkiran.")
            
    elif pilihan == "3":
        parkiran.tampilkan_kendaraan()
        
    elif pilihan == "4":
        jumlah_kendaraan = parkiran.size()
        print(f"Jumlah kendaraan di parkiran: {jumlah_kendaraan}")
        
    elif pilihan == "5":
        if parkiran.is_empty():
            print("Parkiran kosong.")
        else:
            print("Parkiran tidak kosong.")
            
    elif pilihan == "6":
        if parkiran.is_full():
            print("Parkiran penuh.")
        else:
            print("Parkiran tidak penuh.")
            
    elif pilihan == "7":
        parkiran.urutkan_kendaraan()
        if parkiran.is_empty():
            print("Tidak ada kendaraan yang terparkir.")
        else :
            print("Kendaraan di parkiran telah diurutkan sesuai abjad plat nomor.")
        
    elif pilihan == "8":
        if parkiran.is_empty():
             print("Tidak ada kendaraan yang terparkir, silahkan masukkan pilihan 1 untuk memarkirkan kendaraan.")
        else:
            plat_nomor = input("Masukkan Plat Nomor: ")
            position = int(input("Masukkan posisi: "))
            parkiran.insert_kendaraan(plat_nomor, position)
        
    elif pilihan == "9":
        print("Terima kasih telah menggunakan aplikasi parkiran.")
        break
    else:
        print("Pilihan anda tidak valid, silahkan masukan inputan angka.")
