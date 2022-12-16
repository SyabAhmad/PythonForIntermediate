print("List comprehension in python")
import math
squares = []
for i in range(15):
    squares.append( i**2)

print(squares)

values = []
countValues = 0
for i in [1,2,3]:
    for j in [ 4,5,6]:
        if i != j:
            values.append((i,j))
            countValues=countValues+1
print(values)
print("found: ",countValues)


# to take transpose of matrix
list1 = [[1,2,3], [4,5,6], [7,8,9]]
print(list1)
zip(*list1)
print(list1)


