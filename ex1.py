''' We are taking input from the user and using the int function to convert the input into an integer,
and storing the converted input in a variable '''
to_be_divided = int(input("enter the number you want to divide: "))

# Same steps to store a divisor
divisor = int(input("enter the divisor: "))

''' We will use a while-else argument here where the while loop will check whether the divisor is zero and if
the divisor is zero, the user will be prompted to enter another divisor until a valid divisor is provided
and then the calculation will be made. Else, the calculation will be processed directly '''
while divisor == 0:
    print("the divisor should not be zero")
    divisor = int(input("Please enter a valid divisor: "))
else:
    print(to_be_divided / divisor)
    
