for i in range (51):
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

if i > 30:
    print("Panas broo")
else:
    print("Dingin broo")
