# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: # My solution
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        if not head:
            return None
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast==slow:#走道碰頭點了
                while slow!=head:
                    slow=slow.next
                    head=head.next
                return head
                
                
        return None
#%% Other ones solutions
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow = head
        fast = head
        flag = True
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                flag = False
                break
        if flag:
            return None
        while True:
            if slow==head:
                return head
            slow = slow.next
            head = head.next