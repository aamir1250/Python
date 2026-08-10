#!/usr/bin/python3
with open("python.txt","r") as f:
#	f.write("Hi everyone\nwe are learning file I/O\nusing java\ni like programing in python\n")
	data=f.read()
new_data=data.replace("java","python")
print(new_data)
with open("python.txt","w") as f:
	f.write(new_data)
with open("python.txt","r") as f:
	data=f.read()
	if(data.find("jome") != -1):
		print("found")
	else:
		print("not found")
