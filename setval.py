#!/usr/bin/python3

string = "jhanjharpur"

freq = {}

for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

unique = set(freq.keys())
print(unique)
