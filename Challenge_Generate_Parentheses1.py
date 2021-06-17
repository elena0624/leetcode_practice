# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:43:11 2021

@author: ppj
"""

n = 3

ans=[]
ans_str='('
l_b=1
r_b=0

def gen_ans(ans_str,l_b,r_b):
    if l_b+r_b==2*n:
        ans.append(ans_str)
        return
    # +右括號
    if r_b!=l_b and l_b<=n:
        gen_ans(ans_str+')',l_b,r_b+1)
    # +左括號
    if l_b<n:
        gen_ans(ans_str+'(',l_b+1,r_b)
gen_ans(ans_str,l_b,r_b)