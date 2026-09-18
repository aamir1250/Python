#!/usr/bin/python3
def outer():
	x=10
	def inner():
		nonlocal x
		print(x)
		x=x+1
	return inner
fn=outer()
fn()

