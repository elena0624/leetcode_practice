# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # Ugly and redundant answer
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # avoid l1 or l2==None
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        # initialize head
        curl=ListNode()
        l3=ListNode()
        curl.next=l3
        # curl=ListNode()

        if l1.val<=l2.val:
            l3.next=l1
            l1=l1.next
        else:
            l3.next=l2
            l2=l2.next
        l3=l3.next
        # start 
        while l1!=None and l2!=None:
            print('l1',l1)
            print('l2',l2)
            print('l3',l3)
            print('curl',curl)
            if l1.val<=l2.val:
                l3.next=l1
                l1=l1.next
            else:
                l3.next=l2
                l2=l2.next
            l3=l3.next
        print('l1',l1)
        print('l2',l2)
        print('l3',l3)
        
        # if there are still remain
        if l1:
            l3.next=l1
        if l2:
            l3.next=l2
        return curl.next.next
#%% Revised Answer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # initialize head
        curl=ListNode()
        l3=ListNode()
        curl.next=l3
        # start 
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                l3.next=l1
                l1=l1.next
            else:
                l3.next=l2
                l2=l2.next
            l3=l3.next
        
        # if there are still remain
        if l1:
            l3.next=l1
        if l2:
            l3.next=l2
        return curl.next.next
#%% Others answers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2

        head = dummy = ListNode()
        while l1 or l2:
            if not l1:
                head.next = l2
                l2 = l2.next
            elif not l2:
                head.next = l1
                l1 = l1.next
            else:
                if l1.val <= l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next

            head = head.next

        return dummy.next
