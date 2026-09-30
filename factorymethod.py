#!/usr/bin/python3
class FactoryDemo():
	def __init__(self):
		self.age=50
	@staticmethod
	def factory():
		return FactoryDemo()
if __name__ =='__main__':
	obj=FactoryDemo.factory()
	print(obj.age) 
