def myfn():
	x=10
	y=20
	def printer():
		print(x,y)
	return printer
x=myfn()
x()
