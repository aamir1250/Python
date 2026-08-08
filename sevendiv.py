#!/usr/bin/python3
num = int(input("enter a number: "))
rem = num % 7
if(rem == 0):
	print("number is multiple of 7")
elif(rem != 0):
	print("number is not multiple of 7")
