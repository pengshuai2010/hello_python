'''
Created on Jul 27, 2015

@author: speng
'''
import os
import re

def stats(directory, regexp, logfile):
    '''
    find all the files under the specified directory that 
    match the regular expression, write number of lines they
    contain into a log file
    '''
    total_lines = 0
    with open(logfile, 'w') as file_obj:
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                if re.search(regexp, filename):
                    file_obj.write(filename + '\t')
                    fullname = os.path.join(root, filename)
                    with open(fullname) as f:
                        text = f.read()
                        lines = text.count('\n')
                        total_lines = total_lines + lines
                        file_obj.write(str(lines) + '\n')
        file_obj.write('toral lines\t{}'.format(total_lines))

if __name__ == '__main__':
#     directory = '/home/speng/Calix/dash'
    directory = '/home/speng/Calix/workspace'
    stats(directory, r'.py$', '/tmp/file_list.txt')