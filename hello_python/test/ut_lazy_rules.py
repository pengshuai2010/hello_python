'''
Created on Jul 31, 2015

@author: speng
'''
import unittest
import english_plural_3

class Test(unittest.TestCase):


    def test1(self):
        self.assertEqual(english_plural_3.pluralize('computer'), 'computers')
    
    def test2(self):
        self.assertEqual(english_plural_3.pluralize('fox'), 'foxes')

    def test3(self):
        self.assertEqual(english_plural_3.pluralize('coach'), 'coaches')

    def test4(self):
        self.assertEqual(english_plural_3.pluralize('cheetah'), 'cheetahs')

    def test5(self):
        self.assertEqual(english_plural_3.pluralize('toy'), 'toys')

    def test6(self):
        self.assertEqual(english_plural_3.pluralize('vacancy'), 'vacancies')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()