#!/usr/bin/python3
class Superclass:
	def properties(self):
		self.age=30
		self.name="amit kumar"
obj=Superclass()
obj.properties()
print(obj.age)
obj.age=40
print(obj.age)
print(obj.name)
