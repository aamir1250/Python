#!/usr/bin/python3
def cal_sum(n):
	if(n == 0):
		return 0 
	x = cal_sum(n-1)+n
	print(x)
	return x
cal_sum(5)
