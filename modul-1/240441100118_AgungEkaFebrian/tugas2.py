class Mahasiswa:
    def __init__(self, nama, nim, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat

    def tampilkan_data(self):
        print("Data Mahasiswa")
        print(f"Nama   : {self.nama}")
        print(f"NIM    : {self.nim}")
        print(f"Prodi  : {self.prodi}")
        print(f"Alamat : {self.alamat}")
        print()

daftar_mahasiswa = []

jumlah_awal = 3
print("Masukkan minimal 3 data mahasiswa:")
for i in range(jumlah_awal):
    print(f"\nData Mahasiswa ke-{i+1}")
    nama = input("Nama   : ")
    nim = input("NIM    : ")
    prodi = input("Prodi  : ")
    alamat = input("Alamat : ")
    
    mhs = Mahasiswa(nama, nim, prodi, alamat)
    daftar_mahasiswa.append(mhs)


while True:
    tambah = input("\nIngin menambahkan data mahasiswa lagi? (y/n): ").lower()
    if tambah == 'y':
        print(f"\nData Mahasiswa ke-{len(daftar_mahasiswa)+1}")
        nama = input("Nama   : ")
        nim = input("NIM    : ")
        prodi = input("Prodi  : ")
        alamat = input("Alamat : ")
        
        mhs = Mahasiswa(nama, nim, prodi, alamat)
        daftar_mahasiswa.append(mhs)
    elif tambah == 'n':
        break
    else:
        print("Pilihan tidak valid. Ketik 'y' untuk ya atau 'n' untuk tidak.")

print("\nDaftar Mahasiswa yang Telah Diinput\n")
for mahasiswa in daftar_mahasiswa:
    mahasiswa.tampilkan_data()
