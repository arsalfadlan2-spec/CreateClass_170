class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def luas(self):
        return 2 * self.panjang + self.lebar

    def __str__(self):
        return f, {self.panjang}, {self.lebar} 

persegi_panjang = PersegiPanjang(3,2)
print (persegi_panjang)
print (persegi_panjang.keliling(),)
print (persegi_panjang.luas())