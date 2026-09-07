#!/usr/bin/python3
def myfn():
	print("my function called")
	print("leaving myfn")
anothername= myfn
myfn()
anothername()
