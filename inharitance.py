#class object attributes and methods
class Employee:
    raise_amount=1.04
    num_of_emps=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"@company.com"
        Employee.num_of_emps+=1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
emp_1=Employee('Corey','Schafer',50000)
emp_2=Employee('Test','User',60000)
print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(Employee.fullname(emp_1))
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

#inharitance
class Parent:
    def __init__(self):
        print("Parent class constructor")
    def parentMethod(self):
        print("Parent class method")
class Child(Parent): # ada parent dalam child
    def __init__(self):
        print("Child class constructor")
        super().__init__()
    def childMethod(self):
        print("Child class method")
child=Child()
child.childMethod()
child.parentMethod()
print("="*50,"\n")

class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def jalan(self):
        print(f"{self.merk} berwarna {self.warna} sedang berjalan")

# Membuat objek mobil
mobil1 = Mobil("Toyota", "Biru")
mobil1.jalan()  # Output: Toyota berwarna Merah sedang berjalan

class MobilBalap(Mobil):
    def __init__(self, merk, warna, kecepatan):
        super().__init__(merk, warna)
        self.kecepatan = kecepatan

    def turbo(self):
        print(f"{self.merk} menggunakan turbo dengan kecepatan {self.kecepatan} km/jam")

mobil_balap = MobilBalap("Ferrari", "Hot Pink", 300)
mobil_balap.jalan()  # Output: Ferrari berwarna Merah sedang berjalan
mobil_balap.turbo()  # Output: Ferrari menggunakan turbo dengan kecepatan 300 km/jam
print(vars(mobil_balap))
print(dir(mobil1))


print("="*50,"\n")
