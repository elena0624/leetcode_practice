# My solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        cur=ListNode()
        dum=cur
        while head:
            while head and head.val==val:
                head = head.next
            if not head:
                cur.next=None
                break
            cur.next=head
            cur=cur.next
            head=head.next   
        return dum.next
#%% Elegant solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def removeElements(self, head: ListNode, val: int) -> ListNode:
            result =curr = ListNode(-1)
            curr.next = head        
            while curr.next:
                if curr.next.val == val:
                    curr.next = curr.next.next                
                else:
                    curr = curr.next
            return result.next
