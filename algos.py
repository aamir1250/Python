class MyClass:
	def __init__(self):
		self.age=20
#	def getMax(arr):
#	i = 1
#	max = arr[0]
#	while i < len(arr):
#		if arr[i] > max:
#			max = arr[i]
#		i += 1
#	return max

	def getMin(self,arr):
		i=1
		min=arr[0]
		while i<len(arr):
			if arr[i]<min:
				min=arr[i]
			i=i+1
		return min
