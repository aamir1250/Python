#!/usr/bin/python3
def match_char(s1,s2,s3):
	count=0
	if len(s1)<=len(s2) and len(s1)<=len(s3):
		length = len(s1)
	elif len(s2) <= len(s1) and len(s2) <= len(s3):
		length = len(s2)
	else:
		length = len(s3)
	for i in range(length):
		if s1[i] == s2[i] == s3[i]:
			count += 1
		else:
			break
	return count
str1="Lucknow Junction"
str2="Lucknow city"
str3="Lucknow Cantt"
print(match_char(str1,str2,str3))
