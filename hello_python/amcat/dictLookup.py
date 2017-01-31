#!/usr/bin/env python
# DETERMINE CFSFPNJKF TERMINTE
s = raw_input()
words = s.split()
out = ''
mapping = {}
for i in range(len(words[0])):
    mapping[words[0][i]] = words[1][i]
for i in range(len(words[2])):
    out += mapping[words[2][i]]
print out
