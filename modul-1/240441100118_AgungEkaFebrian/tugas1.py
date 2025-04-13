class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"{self.nama} sedang berjalan.")

    def berlari(self):
        print(f"{self.nama} sedang berlari.")

manusia1 = Manusia("Agung", 19, "Bojonegoro")
manusia2 = Manusia("Fajar", 17, "Bojonegoro")
manusia3 = Manusia("Bintang", 1, "Bojonegoro")
manusia4 = Manusia("Melly", 18, "Madura")
manusia5 = Manusia("Eka", 15, "Yogyakarta")

manusia1.berjalan()
manusia2.berlari()
manusia3.berjalan()
manusia4.berlari()
manusia5.berjalan()