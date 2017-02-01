#!/usr/bin/env python
# If BLACK is coded as DNCEM , then ORANGE is coded as QTCPIG
# BLACK   DNCEM   ORANGE
s = raw_input()
words = s.split()
out = ''
for i in range(min(len(words[0]), len(words[1]), len(words[2]))):
    tmp = ord(words[2][i]) - ord(words[0][i]) + ord(words[1][i])
    tmp = (tmp - ord('A') + 26) % 26 + ord('A')
    out += unichr(tmp)
print out
