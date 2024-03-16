# I firstly initialised a variable total with the value zero
total = 0

# Then I chose a for loop as we had to deal with a range of numbers that was finite. My range is inclusive of 23 and 579
for i in range(23, 579):
    # I check whether it is an even number by using a modulo as an even number divided by 2 will have 0 as remainder
    if i % 2 == 0:
        # Then I add the even i to total and the new value is stored inside total.
        # This loop continues until all even numbers in the range are used up.
        total = total + i

# Then I print the total. My print statement is outside the for loop bcoz if it was inside then it would print the total in every iteration.
print(total)