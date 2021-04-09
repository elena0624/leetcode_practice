# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # My solution
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3=ListNode()
        p,q=divmod((l1.val+l2.val),10)
        ls=ListNode(q)
        l3.next=ls
        while l1.next or l2.next:
            if l1.next and l2.next:
                l1=l1.next
                l2=l2.next
                p,q=divmod((l1.val+l2.val+p),10)
            elif l1.next:
                l1=l1.next
                p,q=divmod((l1.val+p),10)                
            else:# l2還有東西
                l2=l2.next
                p,q=divmod((l2.val+p),10)
            ls.next=ListNode(q)
            ls=ls.next
        if p:
            ls.next=ListNode(1)
        return l3.next
#%% Brief Solution
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy 
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 #if l1 has value or nor
            v2 = l2.val if l2 else 0
            
            #new digit
            val = v1 + v2 + carry
            carry = val // 10 
            val = val % 10
            curr.next = ListNode(val)
            curr = curr.next # here we are updating current to the next pointer
            l1 = l1.next if l1 else None # here we are updating list l1 pointer if they are not zero
            l2 = l2.next if l2 else None

        return dummy.next