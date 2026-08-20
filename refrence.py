#!/usr/bin/python3
import sys
import copy
x=10
y=10
a=[2,3,4]
b=[2,3,4]
print(x==y)
print(a==b)
print(a is b)
print(x is y)
a[0]=6
print(a)
print(b)
print(sys.getrefcount(x))
print(sys.getrefcount(b))
z=[9,8,7,[4,6,7],8]
w=copy.deepcopy(z)
w[0]=25
w[3][1]=12
print(z)
print(w)
print(z is w)
x:int
y:int=10
a:list[int]=[2,3,5,1]
y="lucknow"
#print(x)
print(y)
