# -*- coding: utf-8 -*-
"""
Created on Mon May 24 15:30:33 2021

@author: ppj
"""

s = "Hello"

print(''.join(chr(ord(i)+32) if ord(i)>=65 and ord(i)<=90 else i for i in s))