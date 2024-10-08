import keyword as kw
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

a, b, c = 212.1 ,"\n\nBye", 23
print (a)
print (type(a))
print (b)
print (type(b))
print (c)
print (type(c))

x = kw.softkwlist
print(x)