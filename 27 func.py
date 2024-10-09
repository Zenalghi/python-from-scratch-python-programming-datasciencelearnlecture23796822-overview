def greet_user(fname, l_name):
    print(f"Hello {fname} {l_name}!")
    print("Welcome to Python")

print("Start")
greet_user("Minho", 'Albyy')
print("Finish\n")

#28, Methods
class greet:
    def greet_user(self, fname):
        print(f"Hello {fname}!")
        print("Welcome to Python")

wish=greet()
print("Start")
wish.greet_user("Minho")
wish.greet_user("Newt")
print("Finish\n")

#====================================================================
class Person:
    def __init__(self, name):
        self.name=name
    def talk(self):
        print(f"Hi, I am {self.name}")

person1=Person("Minho")
person1.talk()
person2=Person("Albyy")
person2.talk()
print("End")
#====================================================================
#29 list method
numbers=[5,2,1,7,4, 44, 4, 2] # add 2
numbers.append(20) #OUTPUT :[5, 2, 1, 7, 4, 20]
print(numbers)
numbers.insert(0,10) #OUTPUT :[10, 5, 2, 1, 7, 4, 20]
print(numbers)
numbers.remove(5) #OUTPUT :[10, 2, 1, 7, 4, 20]
print(numbers)
numbers.pop() #OUTPUT :[10, 2, 1, 7, 4]
print(numbers)
print(numbers.index(7)) #OUTPUT :3 cari lokasi nilai 7 dimana
print(50 in numbers) #OUTPUT :False
print(numbers.count(4)) #OUTPUT :2
print(44 in numbers) #OUTPUT :True
numbers.sort() #[1, 2, 4, 4, 7, 10, 44]
print(numbers)
numbers.reverse() #[44, 10, 7, 4, 4, 2, 1]
numbers2=numbers.copy()
print(numbers)
numbers.append(100)
print(numbers)  #[44, 10, 7, 4, 4, 2, 1, 100]
print(numbers2) #[44, 10, 7, 4, 4, 2, 1]

print("Finish\n")
#====================================================================
unique=[]
numbers.sort()
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique, 'no one same') #[1, 2, 4, 7, 10, 44, 100]
print(numbers)  #[44, 10, 7, 4, 4, 2, 1, 100]
        
# numbers.clear() #OUTPUT :[]
