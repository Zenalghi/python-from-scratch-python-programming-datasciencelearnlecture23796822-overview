isHot=False

if isHot:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day\n")

isHot=False
isCold=False

if isHot:
    print("It's a hot day")
    print("Drink plenty of water")
elif isCold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day\n")

#25, forloop
for i in 'Python and Jav':
    print(i)
print(type(i))
for d in {'java', 'Ruby','Aqua','Ai'}:
    print(d)
print(type(d))
for l in [1,10,7,6,4]:
    print(l)
print(type(l))

for j in range (4,12,2):
    print(j)

total=0
price=[10,28,10,31,20]
for p in price:
    total+=p
print(f"Total: {total}")

#26, while
i=1
while i<=5:
    # print(i)
    print('*'*i)
    i+=1
print("\nDone")
#27, break and continue
i=0
while i<=5:
    i+=1
    if i==3:
        continue
    print(i)
print("Done")

