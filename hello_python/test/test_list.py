'''
Created on 7/23/2015

@author: speng
'''

if __name__ == '__main__':
    l = range(4)
    print l[-1]
    print filter(lambda x: x % 2 == 0, range(6))
    print map(lambda x: x**3, range(6))
