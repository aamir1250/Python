#!/usr/bin/python3
def countdigits(s):
	count=0
	for a in s:
		if a.isdigit():
			count=count+1
	return count
st="lucknow 3junction4"
c=countdigits(st)
print(c)
