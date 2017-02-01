#!/usr/bin/env python
# calculate difference
# ACFJ CEHL PRUY SUXZ
s = raw_input()
words = s.split()
out = ''
for word in words:
    diff = []
    for i in range(len(word) - 1):
        diff.append(ord(word[i + 1]) - ord(word[i]))
    out += str(diff) + '\t'
print out
