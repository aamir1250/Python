#!/usr/bin/python3
def str_find(num):
	if(num % 2 == 0):
		print("EVEN")
	elif(num % 2 != 0):
		print("ODD")
x=int(input("enter a number: "))
str_find(x)
