#!/usr/bin/python3
info={"firstname":"aamir","lastname":"khursheed","age":20}
for key in info:
	print(info[key])
L=list(info.keys())
for x in L:
	print(info[x])
print(len(info))
