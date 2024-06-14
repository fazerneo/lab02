''' This exercise 3 was an interesting exercise. I initially built a three-dimensional nested if-elif-else
but then I thought, what if the user puts a float or str as an input? I tried and crashed, then I researched
and added the try-except to capture the value error, but again, it would crash if I tried a second value error.
So then I added a while loop and added the code inside the try block so that as long as there is a 
value error, the code will keep looping and asking for a valid integer. I initially tried using the round function
for the floats issue but then thought that the user could add a string also as an input.'''
while True:
    try:
        num = int(input("enter a number between 1 and 7: "))
        if num in range(1,8):
            if num == 1:
                print("Monday")
            elif num == 2:
                print("Tuesday")
            elif num == 3:
                print("Wednesday")
            elif num == 4:
                print("Thursday")
            elif num == 5:
                print("Friday")
            elif num == 6:
                print("Saturday")
            else:
                print("Sunday")
        else:
            print("error: Value is out of range")
        break
    except ValueError:
        print("enter a valid number")
