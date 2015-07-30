'''
Created on Jul 28, 2015

@author: speng
'''

class Fibonacci:
    '''
    generator class of fibonacci sequence
    '''
    def __init__(self, max_value):
        self.max_value = max_value
    
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self
    
    def next(self):
        '''
        the next() method of an iterator class
        note that in python 3, this should be __next__()
        '''
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.max_value:
            raise StopIteration
        return self.a

if __name__ == '__main__':
    for f in Fibonacci(30):
        print f