'''
Created on Jul 28, 2015

@author: speng
'''
import re


def build_match_apply_rules(pat, search, replace):
    def match_rule(word):
        return re.search(pat, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (match_rule, apply_rule)

# using a generator
def rule(rule_file_name):
    with open(rule_file_name) as file_obj:
        for line in file_obj:
            pattern, search, replace = line.split(None, 3)
            yield build_match_apply_rules(pattern, search, replace)

def pluralize(noun):
    for match_rule, apply_rule in rule('plural-rules.txt'):
        if match_rule(noun):
            return apply_rule(noun)
    raise ValueError("no rule for {}".format(noun))

if __name__ == '__main__':

    print pluralize('computer')
    print pluralize('fox')
    print pluralize('coach')
    print pluralize('cheetah')
    print pluralize('toy')
    print pluralize('vacancy')