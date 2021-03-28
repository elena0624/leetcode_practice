# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 23:23:44 2021

@author: ppj
"""

# Reconstruct Original Digits from English
s="owoztneoer"
import collections
# 第一層: z=>zero, w=>two, u=>four, x=>six, g=>eight
# 第二層: 剩下的 f=>five, r=>three
# 第三層: 剩下的 v=>seven, i=>nine
# 剩下的=> one
s_count = collections.Counter(s)
ans_digit = [0]*10

for c, str_dig, pos in [['z','zero',0],['w','two',2],['u','four',4],['x','six',6],['g','eight',8],\
                        ['f','five',5],['r','three',3],\
                        ['v','seven',7],['i','nine',9],\
                        ['o','one',1]]:
#    print(c)
#    print(str_dig)
#    print(pos)
    ans_digit[pos]+=s_count[c]
    for char_dig in str_dig:
#        print(char_dig)
        s_count[char_dig]-=ans_digit[pos]
ans_s=''
for i in range(10):
    ans_s+=str(i)*ans_digit[i]
print(ans_s)
    