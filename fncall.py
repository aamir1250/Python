#!/usr/bin/python3
def called():
	print("called function")
def caller(fn):
	print("caller function")
	fn()
called()
caller(called)
