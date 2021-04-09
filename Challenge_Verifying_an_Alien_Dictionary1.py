# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 15:52:00 2021

@author: ppj
"""

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
ords_dic = {v:k for k,v in enumerate(order)} # 不知道這跟myString.find('s')誰比較快 但後者應該不用多餘的空間 可比比看
for i in range(len(words)-1):
    # 比較前後兩個
    s1=words[i]
    s2=words[i+1]
    s_idx=0
    while s_idx<len(s1):
        if s_idx==len(s2):# s2不能先結束 因為空集合應該在最前面
            print(False)#
            break#
        if ords_dic[s1[s_idx]]>ords_dic[s2[s_idx]]:
            print(False)#
            break#
            # return False
        elif ords_dic[s1[s_idx]]==ords_dic[s2[s_idx]]:
            s_idx+=1
        else:# OK沒問題
            break
print(True)
# return True
#%% Try not to use dict but use find
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
#ords_dic = {v:k for k,v in enumerate(order)} # 不知道這跟myString.find('s')誰比較快 但後者應該不用多餘的空間 可比比看
for i in range(len(words)-1):
    # 比較前後兩個
    s1=words[i]
    s2=words[i+1]
    s_idx=0
    while s_idx<len(s1):
        if s_idx==len(s2):# s2不能先結束 因為空集合應該在最前面
            print(False)#
            break#
        if order.find(s1[s_idx])>order.find(s2[s_idx]):
            print(False)#
            break#
            # return False
        elif order.find(s1[s_idx])==order.find(s2[s_idx]):
            s_idx+=1
        else:# OK沒問題
            break
print(True)