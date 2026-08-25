#!/usr/bin/python3
s="lucknow"
s=s.replace("now","later")
print(s)
city="lucknow"
print(type(city))
city=list(city)
print(type(city))
city[1]="A"
city[2]="B"
city[6]="C"
city.append("Z")
city.append("X")
s1=''.join(city)
print(s)
print(city)
st="lucknow junction"
#st=st.replace('n','p')
#print(st)
a=st.find('n')
b=st[:a]+'p'+st[a+1:]
print(b)
c=st.rfind('n')
print(c)
cities="lucknow-kanpur-rampur-allahabad"
lcities=cities.split("-")
print(lcities)
a=cities.split("pur")
print(a)
z = "lucknow junction"
city = z.split()
print(city)
s1=''.join(city)
print(s1)
