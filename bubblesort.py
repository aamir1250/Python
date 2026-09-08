#!/usr/bin/python3
def asc(L):
	n=len(L)
	for i in range(n):
		for j in range(n-1-i):
			if L[j]>L[j+1]:
				L[j],L[j+1]=L[j+1],L[j]
	return L


def dsc(L):
	n=len(L)
	for i in range(n):
		for j in range(n-1-i):
			if L[j]<L[j+1]:
				L[j],L[j+1]=L[j+1],L[j]
	return L


def sort(L,fn):
	fn(L)
L=[5,3,89,43,54,12,34,56,10,2,1]
print("UNSORTED LIST",L)
sort(L,asc)
print("ACCENDING ORDER SORTED LIST",L)
sort(L,dsc)
print("DECENDING ORDER SORTED LIST",L)
