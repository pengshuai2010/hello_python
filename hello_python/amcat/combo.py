#!/usr/bin/env python
# tests
# DETERMINE CFSFPNJKF TERMINTE
# ACFJ CEHL PRUY SUXZ
# BLACK   DNCEM   ORANGE
def dictLookup(s):
    words = s.split()
    out = ''
    mapping = {}
    for i in range(len(words[0])):
        mapping[words[0][i]] = words[1][i]
    for i in range(len(words[2])):
        out += mapping.get(words[2][i], '?')
    return out


def diff(s):
    words = s.split()
    out = ''
    for word in words:
        diff = []
        for i in range(len(word) - 1):
            diff.append(ord(word[i + 1]) - ord(word[i]))
        out += str(diff) + ', '
    return out


def letter2number(s):
    out = ''
    words = s.split()
    for word in words:
        numbers = []
        for c in word:
            numbers.append(ord(c) - ord('A') + 1)
        out += str(numbers) + ', '
    return out


def plusMinus(s):
    words = s.split()
    out = ''
    for i in range(min(len(words[0]), len(words[1]), len(words[2]))):
        tmp = ord(words[2][i]) - ord(words[0][i]) + ord(words[1][i])
        tmp = (tmp - ord('A') + 26) % 26 + ord('A')
        out += unichr(tmp)
    return out


if __name__ == '__main__':
    s = raw_input()
    print 'dict look up:'
    print dictLookup(s) + '\n'

    print 'plus minus:'
    print plusMinus(s) + '\n'

    print 'diff:'
    print diff(s) + '\n'

    print 'letter 2 number:'
    print letter2number(s) + '\n'
