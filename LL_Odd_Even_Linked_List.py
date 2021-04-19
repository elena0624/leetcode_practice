# My solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dum=head
        dum_e=even_list=head.next
        while head.next:
            head.next=head.next.next            
            if head.next:
                head=head.next
            else:
                break
            even_list.next=even_list.next.next
            if even_list.next:
                even_list=even_list.next
        head.next=dum_e
        return dum
#%% elegant solution
def oddEvenList(self, head):
    dummy1 = odd = ListNode(0)
    dummy2 = even = ListNode(0)
    while head:
        odd.next = head
        even.next = head.next
        odd = odd.next
        even = even.next
        head = head.next.next if even else None
    odd.next = dummy2.next
    return dummy1.next
