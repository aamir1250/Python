#!/usr/bin/python3
list1 = [1,2,1]
list2 = [1,3,2]
copy_list2 = list2.copy()
copy_list2.reverse()
if(copy_list2 == list2):
	print("PALINDROME")
else:
	print("NOT A PALINDROME")
