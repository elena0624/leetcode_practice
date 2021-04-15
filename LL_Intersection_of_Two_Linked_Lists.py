# My solution- Brute force TLE not sure if correct
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a_list=[]
        while headA:
            a_list.append(headA)
            headA=headA.next
        while headB:
            if headB in a_list:
                return headB
            else:
                headB=headB.next
        return None
#%%
# My solution- accepted
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        tempA=headA
        tempB=headB
        while tempA and tempB:
            tempA=tempA.next
            tempB=tempB.next
        headC=headA
        headD=headB
        if tempA or tempB:# 不一樣長
            tempC=tempA if tempA else tempB
            headC=headA if tempA else headB
            headD=headB if tempA else headA
            while tempC:
                tempC=tempC.next
                headC=headC.next
        while headC!=headD:
            headC=headC.next
            headD=headD.next
        return headC
#%% Elegant answer
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA
        # Note: In the case lists do not intersect, the pointers for A and B
        # will still line up in the 2nd iteration, just that here won't be
        # a common node down the list and both will reach their respective ends
        # at the same time. So pA will be NULL in that case.