#/usr/bin/python3
s1="lucknow"
s2="east"
s3=s1+s2
print(s1)
print(s3)
print(s2)
print(s1[:])
L=list(s1)
print(L)
print(s1.find("know"))
print(s1.find("adc"))
s4="kumar"
s5=s1.replace('now','later')
print(s2)
print(s1)
cities="lucknow-unnao-karnataka"
L=cities.split("-")
print(L[2])
print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1)
name=" amit kumar "
print(len(name))
print(len(name.strip()))
print(len(name.lstrip()))
print(len(name.rstrip()))
name="amir"
age=21
stn=f'my name is {name} and age is {age}'
print(stn)
stn='my name is {} and age is {}'.format(name,age)
print(stn)
