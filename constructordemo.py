#!/usr/bin/python3
class Superclass:
	def __init__(self):
		self.age=30
		self.name="amit"
	def printer(self):
		print(self.age,self.name)
class Subclass(Superclass):
	def __init__(self):
		self.age=20
		self.name="fahad"
#class Subclass(Superclass):
#	pass
obj=Superclass()
obj.printer()
