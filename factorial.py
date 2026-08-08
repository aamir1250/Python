#!/usr/bin/python3
n=int(input("any number for factorial: "))
multiply=1
for i in range(1,n+1):
	multiply = multiply*i
print("factorial:",multiply)
