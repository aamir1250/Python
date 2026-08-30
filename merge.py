#!usr/bin/python3
def merge_sort(a,left,right):
	if left	>= right:
		return
	mid=(left+right)//2
	merge_sort(a,left,mid)
	merge_sort(a,mid+1,right)
	merge(a,left,mid,right)
def merge(a,left,mid,right):
	L=a[left:mid+1]
	R=a[mid+1:right+1]
	i=0
	j=0	
	k=left
	while i<len(L) and j<len(R):
		if L[i]<=R[j]:
			a[k]=L[i]
			i=i+1
		else:
			a[k]=R[j]
			j=j+1
		k=k+1
	while i<len(L):
		a[k]=L[i]
		i=i+1
		k=k+1
	while j<len(R):
		a[k]=R[j]
		j=j+1
		k=k+1
a=[2,3,5,7,1,4,8,9]
merge_sort(a,0,len(a)-1)
print(a)
