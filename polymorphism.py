#!/usr/bin/python3
class MyClass:
        age=20
        name="amit kumar"
        def myproc(self):
                print(self.age)
                print(self.name)
obj=MyClass()
obj.myproc()
class MyClass:
	age=20
	name="Aamir"
	def myproc(self):
		print(self.age)
		print(self.name)
	def myproc(self,x,y):
		self.age=x
		self.name=y
		print(self.age)
		print(self.name)
I=MyClass()
I.myproc()
I.myproc(30,"mohit")
