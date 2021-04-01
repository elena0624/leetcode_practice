# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        temp=ListNode(val=head.val)
        temp.next=None
        prev = temp
        cur_node=head
        # print(cur_node.next)
        while cur_node.next!=None:
            cur_node=cur_node.next
            temp=ListNode(val=cur_node.val)
            temp.next=prev
            prev=temp
        return temp
#%% Iterative solution
class Solution:
# @param {ListNode} head
# @return {ListNode}
def reverseList(self, head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev
#%% Recursive Solution
class Solution:
# @param {ListNode} head
# @return {ListNode}
def reverseList(self, head):
    return self._reverse(head)

def _reverse(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self._reverse(n, node)