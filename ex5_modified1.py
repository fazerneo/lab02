''' To modify this exercise, I used a while loop, which takes user input, and if the user input is
at the end, then the loop will break. If it is not "end," then the input will be converted to an integer using the
int cast, and the calculation will be done continuously as it is not supposed to break unless the input is "end".
If there is a value error, then will print, enter a valid value, and continue the loop.'''
while True:
    Fahrenheit = input("enter temperature in Fahrenheit (enter end to exit): ")
    
    if Fahrenheit == "end":
        break
    
    try:
        Fahrenheit = int(Fahrenheit)
        print((Fahrenheit - 32) * 5 / 9)
    except ValueError:
        print("enter a valid value")
