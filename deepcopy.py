#!/usr/bin/python3
d={"data":{"name":"aamir","age":20}}
d2=d.copy()
print(d)
print(d2)
d["data"]["name"]="sumit"
print(d["data"]["name"])
print(d2["data"]["name"])
d.clear()
print(d)
print(d2)
d2["data"]["age"]=35
print(d2["data"]["age"])
del d2["data"]["age"]
print(d2)
