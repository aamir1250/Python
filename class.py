#!/usr/bin/python3
class MyClass:
	name="mohan"
	def setData(self,value):
		self.data=value
	def display(self):
		print(self.data)
#m1=MyClass()
#m1.data="banglore"
#m1.setData("Lucknow")
#m1.data="dss"
#m1.display()
#m2=MyClass()
#m2.setData("kanpur")
#m2.display()
MyClass.data="jaipur"
m1=MyClass()
m2=MyClass()
m2.data="bilaspur"
m1.display()
m2.display()
print(m1.name)
print(m1.name)
print(MyClass.name)
