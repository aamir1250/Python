#!/usr/bin/python3
class Outer:
	class Inner:
		city="kanpur"
		def __init__(self):
			self.city="lucknow"
	def __init__(self):
		self.age=20
		self.name="amit kumar"
		self.objj=Outer.Inner()
	def myfn(self):
		return Outer.Inner()
if __name__=='__main__':
	obj=Outer()
	print(obj.age)
	print(obj.name)
	inner_obj = obj.Inner()
	objj=Outer.Inner()
	print(objj.city)
	#x=obj.myfn()
	print(obj.objj.city)
