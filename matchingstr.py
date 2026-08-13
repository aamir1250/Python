#!/usr/bin/python3
def match_char(s1, s2):
	count=0
	for i in range(len(s1)):
		if s1[i] == s2[i]:
			count += 1
		else:
			break
	return count
str1="Lucknow Junction"
str2="Lucknow city"
print(match_char(str1, str2))
