#!/usr/bin/python3
def dsc(L):
	n=len(L)
	for i in range(n):
		for j in range(n-1-i):
			if L[j]<L[j+1]:
				L[j],L[j+1]=L[j+1],L[j]
	return L
L=[7,21,4,5,8,6,9]
print(dsc(L))
