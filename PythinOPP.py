class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return 2 * self.panjang + self.lebar

    def __str__(self):
        return f"Persegi Panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm" 

input_panjang = int(input("Masukkan Panjang: "))
if input_panjang <= 0:
    print("Panjang harus lebih dari 0")
    exit()

input_lebar = int(input("Masukkan Lebar: "))
if input_lebar <= 0:
    print("Lebar harus lebih dari 0")
    exit()


persegi_panjang = PersegiPanjang(3,2)

print (persegi_panjang)
print ("keliling:",persegi_panjang.keliling(), "cm")
print ("luas:",persegi_panjang.luas(), "cm")