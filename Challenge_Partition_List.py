# My original solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        prev_dum = ListNode()
        prev_L = ListNode()
        prev_dum.next = prev_L
        post_dum = ListNode()
        post_L = ListNode()
        post_dum.next = post_L
        while head:
            if head.val<x:# 接在前面
                prev_L.next=head
                prev_L=prev_L.next
            else:
                post_L.next=head
                post_L=post_L.next
            if head.next==None:
                post_L.next=None
                #print('here')
                break
            head = head.next
        prev_L.next=post_dum.next.next
        return prev_dum.next.next
#%% Revised
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        prev_dum = prev_L = ListNode()
        post_dum = post_L = ListNode()
        while head:
            if head.val<x:# 接在前面
                prev_L.next=head
                prev_L=prev_L.next
            else:
                post_L.next=head
                post_L=post_L.next
            head = head.next
        post_L.next=None
        prev_L.next=post_dum.next

        return prev_dum.next
