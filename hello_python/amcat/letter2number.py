#!/usr/bin/env python
s = raw_input()
words = s.split()
out = ''
for word in words:
    numbers = []
    for c in word:
        numbers.append(ord(c) - ord('A') + 1)
    out += str(numbers) + '\t'
print out
