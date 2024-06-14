# I first initialized a variable total with the value of zero
total = 0

# Then, I chose a for loop as we had to deal with a finite range of numbers. My range is inclusive of 23 and 579
for i in range(23, 579):
    # I check whether it is an even number by using a modulo as an even number divided by 2 will have 0 as the remainder
    if i % 2 == 0:
        # Then I add the even i to the total, and the new value is stored inside the total.
        # This loop continues until all even numbers in the range are used up.
        total = total + i

# Then I print the total. My print statement is outside the for loop because if it were inside, it would print the total in every iteration.
print(total)
