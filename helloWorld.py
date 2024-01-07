def func(x):
    if x == 1:
        return 1
    else:
        return x*func(x-1)


var = int(input("What is the number you wish to calculate: "))

while var <= 0:
    print("\nError, Enter correct input!!\n")
    var = int(input("What is the number you wish to calculate: "))

print(str(var)+"! = "+str(func(var)))
