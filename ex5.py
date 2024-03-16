#!/usr/bin/env python

#Taking integer inputs from users for the calculations. I made a for loop for 7 times as I wanted to make 7 calculations
for i in range( 7):
	fahrenheit = int(input("enter temperature in fahrenheit: "))
#Printing the celsius value using the given formula
	print((fahrenheit - 32) * 5 / 9)
