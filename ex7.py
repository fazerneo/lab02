# I am using the while loop with try-except again to catch errors.
while True:
    try:
        # We take inputs for the range and store them inside two variables
        range_start = int(input("enter the start of your range: "))
        range_end = int(input("enter the end of your range, remember that the range will be exclusive of this number: "))

        # We initialize a variable total with 0 as the value
        total = 0

        # We check if the range makes sense by checking whether the range start is smaller than the range end
        if range_start < range_end:
            # Then we run a for loop as this is a finite range. We use the variables directly in the range function
            for i in range(range_start, range_end):
                # I check whether it is an even number by using a modulo as an even number divided by 2 will have 0 as the remainder
                if i % 2 == 0:
                    # Then I add the even i to the total, and the new value is stored inside the total.
                    # This loop continues until all even numbers in the range are used up.
                    total = total + i

            # Then I print the total. My print statement is outside the for loop because if it was inside, it would print the total in every iteration.
            print(total)
            break
        # If the range start and range end does not make sense, then this else statement is called
        else:
            print("enter a valid range next time")
        # The loop is broken when a successful calculation is made
        
    # If there is a value error, it will continually loop until a proper calculation is made.
    except ValueError:
        print("your values need to be valid integers")
