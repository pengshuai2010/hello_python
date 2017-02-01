#!/usr/bin/env python
# solve right-angled triangle
# test: a = 19, b = 24, then c = 30.6
import math

s = raw_input()
words = s.split()
a = float(words[0])
b = float(words[1])
print math.sqrt(a * a + b * b)
