#!/usr/bin/python3
def reverseList(list):
	flag=0
	i=0
	j=len(list)-1
	while i>j:
		list[i],list[j]=list[j],list[i]
		i=i+1
		j=j-1
	else:
		if flag == 0:
			print("condition not met")
L=[2,3,5,6,7,9]
print(L)
reverseList(L)
print(L)
