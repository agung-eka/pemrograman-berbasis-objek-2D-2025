class Kucing:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def suara(self):
        print(f"{self.nama} (warna {self.warna}) mengeong: Meong!")


class Anjing:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def suara(self):
        print(f"{self.nama} (jenis {self.jenis}) menggonggong: Guk guk!")


class Burung:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def suara(self):
        print(f"{self.nama} (asal {self.asal}) berkicau: Cuit cuit!")


data_kucing = [("Milo", "Putih"), ("Luna", "Hitam"), ("Oyen", "Orange")]
data_anjing = [("Bruno", "Bulldog"), ("Rocky", "Labrador"), ("Sky", "Husky")]
data_burung = [("Rio", "Papua"), ("Pino", "Kalimantan"), ("Tia", "Sumatera")]

print("== Kucing ==")
for nama, warna in data_kucing:
    kucing = Kucing(nama, warna)
    kucing.suara()

print("\n== Anjing ==")
for nama, jenis in data_anjing:
    anjing = Anjing(nama, jenis)
    anjing.suara()

print("\n== Burung ==")
for nama, asal in data_burung:
    burung = Burung(nama, asal)
    burung.suara()
