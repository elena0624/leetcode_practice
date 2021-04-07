# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:56:13 2021

@author: ppj
"""
import collections
s = "MerryChristmas"

print(not bool(sum(collections.Counter(s[:len(s)//2])[x] for x in ['A','E','I','O','U','a','e','i','o','u'])-sum(collections.Counter(s[len(s)//2:])[x] for x in ['A','E','I','O','U','a','e','i','o','u'])))