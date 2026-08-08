#!/usr/bin/python3
search=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter number you have to find: "))
i=0
while i<len(search):
	if(search[i] == x):
		print("FOUND AT IDX:",i)
		break
	i+=1
	if i == len(search):
		print("NOT FOUND")
