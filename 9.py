#part 2 no.9
print ("hello world\n")

#part 3 no.12
#Datatype

x = type(2)
print(x)
#output: <class 'int'>
y=type("Halo Dunia!")
print(y)
#output: <class 'str'>
z=type(20.5)
print(z)
#output: <class 'float'>
a=type(1j)
print(a)
#output: <class 'complex'>
b=type(["apple", "banana", "cherry"])
print(b)
#output: <class 'list'>
c=type(("apple", "banana", "cherry"))
print(c)
#output: <class 'tuple'>
d=type(range(6))
print(d)
#output: <class 'range'>
e=type({"name" : "John", "age" : 36})
print(e)
#output: <class 'dict'>
f=type({"apple", "banana", "cherry"})
print(f)
#output: <class 'set'>
g=type(frozenset({"apple", "banana", "cherry"}))
print(g)
#output: <class 'frozenset'>
h=type(True)
print(h)
#output: <class 'bool'>
i=type(b"Hello")
print(i)
#output: <class 'bytes'>
j=type(bytearray(5))
print(j)
#output: <class 'bytearray'>
k=type(memoryview(bytes(5)))
print(k)
#output: <class 'memoryview'>

x= 1+2
print("1 + 2 =", x)
#1 + 2 = 3
x= 2-1
print(x)
#1
x= 3*4
print(x)
#12
x= 3/2
print(x)
print(type(x))
#2.0
x= 5%2
print(x)
#1
x= 6//2
print(x)
#3
x= 2**2
print(x)
#4
x= 2**3
print(x)
#8
