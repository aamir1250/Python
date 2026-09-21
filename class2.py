#!/usr/bin/python3
class MyClass:
	def setData(self,value):
		self.data=value
	def display(self):
		print(self.data)
class MClass(MyClass):
	def show(self):
		print("kanpur")
		#print(self.data)
m=MClass()
m.setData("ALLAHABAD")
m.display()
#m.show()
