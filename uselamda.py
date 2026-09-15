#!/usr/bin/python3
marks=[90,50,100,150,20]
dmarks=list(map(lambda x:x*2,marks))
print(marks)
print(dmarks)
evenmarks=filter(lambda x:x%2==0,marks)
print(list(evenmarks))
