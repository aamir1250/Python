#!/usr/bin/python3
class Superclass:
	def add(self,x,y):
		return x + y
	def sub(self,x,y):
		return x - y
class Subclass(Superclass):
	def sum(self,x,y,z):
		return x + y + z
	
obj=Subclass()
print(obj.add(2,5))
print(obj.sub(5,2))
print(obj.sum(2,1,5))
