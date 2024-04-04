# lab02
week 2 python lab

Exercises

1. Write a simple program that reads two integer numbers from the keyboard and then divides one by the other using integer division and then reports the result. Note you should store both inputs into variables and confirm that the second number (i.e. the divisor) is not zero; this confirmation should be done before actually performing the division, as division by 0 is not mathematically defined and will cause your program to crash. You should also store the result of the integer division in a variable and print it out.

2. Add to the simple program from Exercise 1 such that after performing and reporting the division result, it calculates, stores and reports the remainder of the integer division of the same two input integer numbers. Hint: use the modulas operator.

3. Write a simple program that reads in an integer between 1 and 7 inclusive and prints out the corresponding day of the week, assuming Monday is 1, Tuesday is 2, etc. You should use a nested if--elif-else statement as part of your solution. Provide a default "else" for when the entered number is outside the required range.

4. Write a program using if-elif-else statements that simulates the fines issued to drivers based on speeds recorded by a police radar gun.

Your program should read the recorded vehicle speed (in km/h) as an integer and print the message "Speeding" if the speed exceeds 60 km/h or "Not Speeding" if the speed 60 km/h or less.

The program should then calculate the appropriate fine (if applicable). If the speed is 5 km/h or less over this limit, only issue a warning. If the speed is more than 5 and no more than 10 km/h above the limit, the fine is $100. For a speed of more than 10 but no more than 20 km/h above the limit, the fine is $200. For a speed of more than 20 km/h above the limit, the fine is $500.

You should consider what to do if the input is a negative number. Speed cameras do not register negative numbers, so they should not be accepted as input.

Note: data type is assumed to be int (i.e. and integer); for the purpose of this exercise, DO NOT use floating point numbers.

Also, 60 or less means the speed can be 60 but no more; this is not speeding. Exceeds 60 means the speed is over 60 and therefore speeding. This same logic applies when considering the other speed categories and can be viewed as follows:

61-65 inclusive = warning
66-70 inclusive = $100
71-80 inclusive = $200
81 or more = $500

5. Modify Exercise 5 in Lab 1 using a while loop: the program will repeatedly read a user input as the temperature value in Fahreinheit, and convert it to Celsius and print it out, until the user input is "end".

6. Write a program to calculate the sum of all even numbers between 23 and 578. Hints: which loop would you use, while or for?

7. Revise Exercise 6 above, so that your program can calculate the sum of all even numbers between any two numbers. You should prompt the user to enter the two numbers. You must check the two numbers to ensure they make sense for this question.

8. Research: in Topic 2, we mentioned operator == to compare two values to see whether they are equal. Python has another operator is for similar purpose. Conduct a research to find out the similarity and difference between the two operators.
