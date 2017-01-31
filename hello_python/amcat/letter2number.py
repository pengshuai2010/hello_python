s = raw_input()
out = ''
for i in range(len(s)):
    if s[i] != ' ':
        out += str(ord(s[i]) - ord('A'))
        out += ','
    else:
        out += '\t'
print out
