#!/usr/bin/env python
# test: input CE 1, output DF
s = raw_input()
words = s.split()
letters = words[0]
shift = int(words[1])
shift %= 26
out = ''
for c in letters:
    out += unichr(ord('A') + (ord(c) - ord('A') + shift) % 26)
print out
