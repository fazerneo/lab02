#!/usr/bin/env python

#Taking integer inputs from users for the calculations. I made a for loop for 7 times as I wanted to make 7 calculations
for i in range( 7):
	Fahrenheit = int(input("enter temperature in Fahrenheit: "))
#Printing the Celsius value using the given formula
	print((Fahrenheit - 32) * 5 / 9)
