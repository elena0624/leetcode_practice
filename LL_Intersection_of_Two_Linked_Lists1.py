# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:18:56 2021

@author: ppj
"""
# 本來試著想都reverse之後比對，但無法在不動到原來架構的情況下倒轉
# 錯誤答案留個紀念

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # cur record for head
        # rev record for reverse list
        cur_a=None
        rev_a=None
        temp_a=ListNode(headA.val)
        temp_a.next=headA.next
        while temp_a:            
            cur_a=temp_a
            temp_a=temp_a.next
            cur_a.next=rev_a
            rev_a=cur_a
        print(rev_a)
        
        cur_b=None
        rev_b=None
        while headB:            
            cur_b=headB
            headB=headB.next
            cur_b.next=rev_b
            rev_b=cur_b
        print(rev_b)
        
        
#%%
