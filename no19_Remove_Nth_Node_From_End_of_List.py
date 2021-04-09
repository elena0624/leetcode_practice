# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # My solution
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        target=ListNode()
        fast=head
        target.next=head
        for i in range(n-1):# fast先往前走n-1步
            fast=fast.next
        if not fast.next:#代表n=sz
            target.next=head.next
            return target.next
        # 其他情形
        while fast.next.next:# head.fast一起走,直到fast抵達終點前一步,此時head的位置就是從後數回來的n個前一個位置
            head=head.next
            fast=fast.next
        head.next=head.next.next if head.next.next else None # 把head前一個位置接到下下個位置上 如果下個位置就是底了那就接到None
        return target.next
#%% brief solutions
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head