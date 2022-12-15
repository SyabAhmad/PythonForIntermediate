print("Control flow tools in python")
# if statement
age = 21
if age >18:   # to check whither the condition is tru or nor
    print("You are Welcome") # if true will print this
elif age <18:   # to check whither the condition is tru or nor
    print("You are Kid")  # if true will print this
else:   # to check whither the condition is tru or nor
    print("Old Enough")  # if true will print this


# for Statement
value = [10,20,23,42]
for i in value:
    print(i)

for i in range(10):
    print(i)


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# sum range
print(sum(range(4)))

for i in range(2, 10):
    for x in range(2, i):
        if i%x == 0:
            print(i, " equals ", x, " * ", i//x)
            break
        else:
            print("is prime Number")


#to find a even and odd number by using for loop

for i in range(1,10):
    if i%2 == 0:
        print("Found in even Number: ", i)
    else:
        print("Odd Number found: ", i)


# match statement in python
def options(option):
    match option:
        case 1:
            return "great"
        case 2:
            return "great"
        case 3:
            return "great"
# or you will also write
        case 1| 2|3:
            return "TRUE"

# febonacci series
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a , b = b , a+b
        return result

fib1 = fib2((100))
print(fib1)