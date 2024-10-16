#Encapsulation
class lappy():
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price
l = lappy() #save class yang diatas
l.sell() #output 900
l.__maxprice = 1000 #output 900
l.sell() #output 900
l.setMaxPrice(1000) #output 1000
l.sell() #output 1000
print("="*50,"\n")

class BankAccount:
    def __init__(self, saldo):
        self.__saldo = saldo  # Ini adalah variabel privat (tersembunyi)

    def cek_saldo(self):
        return self.__saldo  # Hanya bisa dicek melalui metode ini

    def setoran(self, jumlah):
        self.__saldo += jumlah
        print(f"Setoran sebesar {jumlah} berhasil.")

rekening = BankAccount(1000)
print(rekening.cek_saldo())  # Output: 1000
rekening.__saldo=50000000000
rekening.setoran(500)
print(rekening.cek_saldo())  # Output: 1500
print("="*50,"\n")

#Polymorphism

class Shark:
    def swim(self):
        print("The shark is swimming.")
    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")
    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")
class Clownfish:
    def swim(self):
        print("The clownfish is swimming.")
    def swim_backwards(self):
        print("The clownfish can swim backwards.")
    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")
sammy = Shark()
sammy.skeleton()
casey = Clownfish()
casey.skeleton()
print("="*50,"\n")
class Kucing:
    def suara(self):
        print("Meong!")

class Anjing:
    def suara(self):
        print("Guk Guk!")

def buat_suara(hewan):
    hewan.suara()

kucing = Kucing()
anjing = Anjing()

buat_suara(kucing)  # Output: Meong!
buat_suara(anjing)  # Output: Guk Guk!


