print("List comprehension in python")

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
