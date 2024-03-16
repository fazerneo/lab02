''' To modify this exercise, I used a while loop which will take a user input and if the user input is 
end, then the loop will break. If it is not end then the input will be converted to an integer using the
int function and the calculation will be done continuously as it is not supposed to break unless input is end.
If there is value error then will print enter a valid value and continue the loop.'''
while True:
    fahrenheit = input("enter temperature in fahrenheit (enter end to exit): ")
    
    if fahrenheit == "end":
        break
    
    try:
        fahrenheit = int(fahrenheit)
        print((fahrenheit - 32) * 5 / 9)
    except ValueError:
        print("enter a valid value")