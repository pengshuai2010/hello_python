'''
Created on Jul 30, 2015

@author: speng
'''
import re

def build_match_apply_rules(pat, search, replace):
    def match_rule(word):
        return re.search(pat, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (match_rule, apply_rule)

class Lazy_rules:
    '''
    generate match_rule function and apply_rule function
    of pluralize()
    '''
    rule_file = 'plural-rules.txt'

    def __init__(self):
        self.cache = []
        self.file_obj = open(self.rule_file)
    
    def __iter__(self):
        self.cache_index = 0
        return self
    
    def next(self):
        self.cache_index += 1
        if self.cache_index > len(self.cache):
            if self.file_obj.closed:
                raise StopIteration()
            line = self.file_obj.readline()
            if line:
                pattern, search, replace = line.split(None, 3)
                self.cache.append(build_match_apply_rules(pattern, search, replace))
                return self.cache[self.cache_index - 1]
            self.file_obj.close()
            raise StopIteration()
        return self.cache[self.cache_index - 1]

def pluralize(noun):
    for match_rule, apply_rule in Lazy_rules():
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
            
            
        
        