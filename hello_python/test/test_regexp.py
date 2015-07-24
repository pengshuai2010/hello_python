'''
Created on 7/22/2015

@author: speng
'''
import re


def check_valid_roman_number(roman_number):
    pattern = r"""^     #beginning
            M{,3}    #thousands
            (CD|CM|D?C{,3})    #hundreds
            (XL|XC|L?X{,3})    #tens
            (IV|IX|V?I{,3})    #ones
            $    #end"""
    pat = re.compile(pattern, re.VERBOSE)
    return pat.search(roman_number) is not None


def extract_phone_number(phone_number):
    pattern = r"""(\d{3})\D*(\d{3})\D*(\d{4})\D*\d*"""
    match = re.search(pattern, phone_number)
    if match:
        return match.groups()
    else:
        return None
if __name__ == '__main__':
    mail_pat = re.compile(r'([\w\-.]+)@([\w.]+)')
    mail_pat = re.compile(r"""([\w\-.]+) # user name
                            @            # the @ symbol
                            ([\w.]+)    # domain name""", re.VERBOSE)
    s = "s.peng_-2010@gmail.com"
    match = mail_pat.search(s)
    print match.group()
    print match.group(1)
    print match.group(2)
    # check roman number
    print check_valid_roman_number("MMXVI")  # 2015
    print check_valid_roman_number("MCMXCIX")  # 1999
    print check_valid_roman_number("I")  # 1
    print check_valid_roman_number("MCMXCIXX")  # invalid
    # check phone number
    print extract_phone_number("(800)5551212 x1234")
    print extract_phone_number("800-555-1212 ext. 1234")
    print extract_phone_number("work 1-(800) 555.1212 #1234")
