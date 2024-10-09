#formatting string / f string
first='alice'
last = 'mary'
message = first + last + 'is a software engineer'
print(message)
msz=f'{first} {last} is a gamer'
print(msz)

# 19, list
name=['alice','thomas','minho', 'newt','Tessera',"peter"]
print(name)
print(type(name))
print(name[0])
print(name[1])
print(name[2])
print(name[3])

print("\n")

print(name[-1])
print(name[-2])
print(name[-5])
name[0]='Alya'
print(name[2:])
print(name[0:3])

no=[1,22,33,42,55,661,321,71]
# no[0]=23
print(no)
print(type(no))
max = no[0]
for i in no:
    if i>max:
        max=i
print(max)

#19.5, list method
name.append('james')
print(name)
name.insert(1,'jane')
print(name)
name.remove('newt')
print(name)
name.pop()
print(name)
name.pop(1)
print(name)
name.clear()
print(name)
print("\n\n")

#20, dictionary
customer = {
    "name":"john",
    "age":30,
    "is_verified":True
}
print(customer)
print(type(customer))
print(customer["name"])
print(customer["age"])
print(customer["is_verified"])
print("\n\n")
print(customer.get("name"))
print(customer.get("age"))
print(customer.get("is_verified"))
print("\n\n")
print(customer.get("birthdate")) #none

customer["name"]="jane"
print(customer)

#20.5, dictionary method
print(customer.items())
print(customer.keys())
print(customer.values())
print("\n")
for key in customer:
    print(key)
print("\n")
for key in customer:
    print(key, customer[key])

print("\n")

for key, value in customer.items():
    print(key, value)

print("\n")

print(customer.pop("name"))
print(customer)
print(customer.popitem())
print(customer)
customer["name"]="john"
print(customer)
customer.update({"name":"jane","age":32})
print(customer)
customer.clear()
print(customer)
print("\n")

#21, tuple
point=(1,2,3)
print(point)
print(type(point))
print(point[0])
print(point[-1])
print("\n")

nama = ('alice','thomas','minho', 'newt','Tessera',"peter")
l = list(nama)
l[1] = 'Chuck'
namaaa = tuple(l)
print(namaaa)
print(type(namaaa))
print("\n")

for n in namaaa:
    print(n)



