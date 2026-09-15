#!/usr/bin/python3
def myfn(x):
	print("lucknow")
	x()
def abc():
	print("kanpur")
myfn(abc)
abc()
myfn(lambda:print("kanpur"))
