# 30, nest loop x, y
for x in range(1, 4):
    for y in range(1, 4):
        print(f'({x}, {y})')
    print('\n')
print("Done")
#====================================================================
num=[5,2,5,2,2]
for i in num:
    print('*'*i)

for i in num:
    output=''
    for j in range(i):
        output+='*'
    print(output)
print("="*50,"\n")

# 31, 2D list use nest loop
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1]) #1
print("="*50,"\n")

# matrix [0][1]=31
# print(matrix[0][1]) #1

for row in matrix:
    for item in row:
        print(item)