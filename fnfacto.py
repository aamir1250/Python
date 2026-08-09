#!/usr/bin/python3
def fact_n(list):
	n = 1
	for i in list:
		n = n * i
	print(n)
	return n
fact_n([1,2,3,4,5])
