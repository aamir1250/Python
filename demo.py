#!/usr/bin/python3
class MyClass:
#	def __init__(self):
		age=20
		name="amit kumar"
class ChildClass(MyClass):
#	def __init__(self):
		city="lucknow"
#		super().__init__()
if __name__=='__main__':
	obj=ChildClass()
	print(obj.city)
	print(obj.age)
	print(obj.name)
