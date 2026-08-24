#!/usr/bin/python3
def recursive_insertion(a,n):
	if n<=1:
		return
	recursive_insertion(a,n-1)
	key=a[n-1]
	j=n-2
	while j>=0 and a[j]>key:
		a[j+1]=a[j]
		j-=1
	a[j+1]=key
a=[12,8,1,23,11,3,5,6]
recursive_insertion(a,len(a))
print("Sorted array:",a)
