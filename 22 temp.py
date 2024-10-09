#22, comparison operator
for i in range (-5,10):
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
    if i >= 30:
         print("Panas broo\n")
    else:
         print("Dingin broo\n")

temp = 22
if temp != 30:
         print("Panas broo\n")
else:
         print("Dingin broo\n")

#input name
while True:
    name = "Sakura"  #input("Enter your name: ")

    if len(name) <= 3:
        print("Name must be more than 3 characters.\n")
    elif len(name) >= 50:
        print("Name must be less than 50 characters.\n")
    else:
        print("Name is Good!\nHello, " + name + "!\n")
        break  
#23, logical operator
has_high_income=True
has_good_credit=True
if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

has_high_income=True
has_criminal_rec=False
if has_high_income and not has_criminal_rec:
    print("Eligible for loan")
else:
    print("Not eligible for loan")