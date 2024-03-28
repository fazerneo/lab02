''' I used the same while loop with the try-except block as from exercise 3. I recorded the speed and
gave a special note for it to be only the digits instead of something like 60 kmph. I thought it 
could be possible to use such an input too but upon research found that it would be too much of a headache.'''

# Please remember to break the loop. Haha
while True:
    try:
        # so we record the speed in a variable speed as an integer. We give a special note to only use digits
        speed = int(input("enter the recorded speed (Note: just enter the digits(example: 60 instead of 60 kmph)): "))

        # Then we use an if-elif-else to check whether the person is speeding, not speeding or if the speed is negative, then it is invalid.
        if speed > 60:
            print("Speeding")
            # Then we use a nested if-elif-else to give warning or fines.        
            if speed > 60 and speed <= 65:
                print("Warning yoe marey")
            elif speed >= 65 and speed <= 70:
                print("pay a fine of $100")
            elif speed > 70 and speed <= 80:
                print("pay a fine of $200")
            else:
                print("pay a fine of $500")
        elif speed < 0:
            print("not a valid speed")
        else:
            print("not speeding")
        break
    # A value error will occur if we enter a float or string when the variable is expecting an integer
    except ValueError:
        print("enter a valid speed, such as 60, 61, 128. Values like 1.2, 61.5, sixty is not valid")