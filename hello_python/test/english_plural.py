'''
Created on Jul 28, 2015

@author: speng
'''
import re

# def pluralize(word):
#     if re.search(r'[sxz]$', word):
#         return re.sub('$', 'es', word)
#     elif re.search(r'[^aeioudgkprt]h$', word):
#         return re.sub('$', 'es', word)
#     elif re.search(r'[^aeiou]y$', word):
#         return re.sub('y$', 'ies', word)
#     else:
#         return re.sub(r'$', 's', word)


def build_match_apply_rules(pat, search, replace):
    def match_rule(word):
        return re.search(pat, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (match_rule, apply_rule)

# separate data from code
rules = []
with open('plural-rules.txt') as file_obj:
    for line in file_obj:
        pattern, search, replace = line.split(None, 3)
        rules.append(build_match_apply_rules(pattern, search, replace))

def pluralize(noun):
    for match_rule, apply_rule in rules:
        if match_rule(noun):
            return apply_rule(noun)

if __name__ == '__main__':

    print pluralize('computer')
    print pluralize('fox')
    print pluralize('coach')
    print pluralize('cheetah')
    print pluralize('toy')
    print pluralize('vacancy')