#!/usr/bin/python3
class MyClass:
	age=30
	def add(self,x,y):
		return x+y
print(list(MyClass.__dict__))
#print(MyClass["age"])
print(MyClass.__dict__["age"])
m=MyClass()
#print(m.__dict__["age"])
print(list(m.__dict__))
m.name="amit singh"
print(list(m.__dict__))
print(m.name)
print(m.age)
print(m["name"])
print(m["age"])
