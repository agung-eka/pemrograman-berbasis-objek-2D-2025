class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not MataKuliah.cek_sks(sks):
            raise ValueError(f"SKS {sks} tidak valid. Harus 2 atau 3.")
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def cek_sks(sks):
        return sks in [2, 3]

class Kampus:
    total_mahasiswa = 0

    def __init__(self, nama, alamat):
        if not Kampus.cek_nama_kampus(nama):
            raise ValueError("Nama kampus tidak valid, tidak boleh mengandung angka.")
        self.nama = nama
        self.alamat = alamat

    def tampilkan_info_kampus(self):
        print(f"Nama Kampus     : {self.nama}")
        print(f"Alamat Kampus   : {self.alamat}")
        print(f"Total Mahasiswa : {Kampus.total_mahasiswa}")

    @staticmethod
    def cek_nama_kampus(nama):
        return not any(char.isdigit() for char in nama)

class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            raise ValueError(f"NIM {nim} tidak valid.")
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.matkul_diambil = []
        Mahasiswa.jumlah_mahasiswa += 1
        Kampus.total_mahasiswa += 1

    def tambah_matkul(self, matkul):
        self.matkul_diambil.append(matkul)

    def tampilkan_info(self):
        print(f"\nNama   : {self.nama}")
        print(f"NIM    : {self.nim}")
        print(f"Prodi  : {self.prodi}")
        print("Mata Kuliah yang diambil:")
        for matkul in self.matkul_diambil:
            print(f"- {matkul.nama} ({matkul.kode}) - {matkul.sks} SKS")

    @classmethod
    def tampilkan_jumlah_mahasiswa(cls):
        print(f"\nTotal Mahasiswa: {cls.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nim(nim):
        return nim.startswith("23") and len(nim) == 10

# ---------- Bagian Program Utama ----------

# Buat objek MataKuliah (minimal 8)
matkul1 = MataKuliah("MK001", "PBO", 3)
matkul2 = MataKuliah("MK002", "Basis Data", 3)
matkul3 = MataKuliah("MK003", "Algoritma", 2)
matkul4 = MataKuliah("MK004", "Web", 3)
matkul5 = MataKuliah("MK005", "Jaringan", 2)
matkul6 = MataKuliah("MK006", "PBD", 3)
matkul7 = MataKuliah("MK007", "Statistik", 2)
matkul8 = MataKuliah("MK008", "Alpro", 3)

daftar_matkul = [matkul1, matkul2, matkul3, matkul4, matkul5, matkul6, matkul7, matkul8]

# Buat objek Kampus dengan alamat
kampus1 = Kampus("Universitas Trunojoyo Madura", "JL. Raya Tellang")

# Buat objek Mahasiswa (minimal 6)
mahasiswa1 = Mahasiswa("Ali", "2312345678", "Sistem Informasi")
mahasiswa2 = Mahasiswa("Budi", "2312345679", "Teknik Informatika")
mahasiswa3 = Mahasiswa("Citra", "2312345680", "Sistem Informasi")
mahasiswa4 = Mahasiswa("Dewi", "2312345681", "Teknik Komputer")
mahasiswa5 = Mahasiswa("Eka", "2312345682", "Manajemen Informatika")
mahasiswa6 = Mahasiswa("Fajar", "2312345683", "Sistem Informasi")

# Tambahkan minimal 4 matkul ke masing-masing mahasiswa
for mhs in [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4, mahasiswa5, mahasiswa6]:
    mhs.tambah_matkul(matkul1)
    mhs.tambah_matkul(matkul2)
    mhs.tambah_matkul(matkul3)
    mhs.tambah_matkul(matkul4)

# Tampilkan info semua mahasiswa
print("=== Informasi Mahasiswa ===")
for mhs in [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4, mahasiswa5, mahasiswa6]:
    mhs.tampilkan_info()

# Tampilkan info kampus
print("\n=== Informasi Kampus ===")
kampus1.tampilkan_info_kampus()

# Tampilkan semua mata kuliah
print("\n=== Daftar Semua Mata Kuliah ===")
for matkul in daftar_matkul:
    print(f"{matkul.kode} - {matkul.nama} ({matkul.sks} SKS)")
