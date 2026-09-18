#!/usr/bin/python3
x=10
def myfn():
	global x
	x=20
	print(x)
	def mf():
		global x
		x=30
		print(x)
	mf()
myfn()
print(x)
