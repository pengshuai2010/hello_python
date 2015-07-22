'''
Created on Jul 22, 2015

@author: speng
'''
import os
import glob

if __name__ == '__main__':
    print os.getcwd()
    homedir = os.path.expanduser('~')
    path = os.path.join(homedir, 'java_programs/*.java')
    print [(os.path.split(f)[1], os.stat(f).st_size) for f in glob.glob(path)]
    print {os.path.split(f)[1]: os.stat(f).st_size for f in glob.glob(path)}