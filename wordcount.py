#!/usr/bin/python3
def count_words(s):
	count = 0
	for i in range(len(s)):
		if s[i] == " " or s[i] == "\n":
			count += 1
	return count +1 
s = "Hi everyone \nwe are learning Python"
print(count_words(s))
