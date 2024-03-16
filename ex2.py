''' We are taking an input from the user and using the int function to convert the input into an integer,
and storing the converted input in a variable '''

dividend = int(input("enter the number you want to divide: "))

# Same steps to store a divisor
divisor = int(input("enter the divisor you want to use to divide the dividend: "))

''' We wil use a while-else argument here where the while loop will check whether the divisor is zero and if
the divisor is zero, the user will be prompted to enter another divisor again and again until a valid divisor is provided
and then the calculation will be made. Else the calculation will be processed directly.
In this exercise, we also calculate the remainder and print i out'''
while divisor == 0:
    print("the divisor should not be zero")
    divisor = int(input("please enter a valid divisor: "))
else:
    result = dividend / divisor
    print("the result of the division is: ", result)
    remainder = dividend % divisor
    print("the remainder is: ", remainder)