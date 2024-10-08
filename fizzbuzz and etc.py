for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 2 == 0:
        print(i, "adalah angka genap")
    else:
        print(i, "adalah angka ganjil")

