# Palindrome Linked List
# Accepted but slow
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ori_list=[head.val]
        # re_list=[head.val]
        cur_node=head
        while cur_node.next:
            cur_node=cur_node.next
            ori_list.append(cur_node.val)
            #re_list.insert(0,cur_node.val) # insert會太花時間?
            
        #if ori_list==re_list:# ==會太花時間?
        if ori_list  == ori_list[::-1]:
            return True
        else:
            return False
#%% First reverse then compare head and reverse node, slow!!!
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev_node = ListNode(val=head.val)
        prev_node = rev_node
        cur_node = head
        while cur_node.next:
            # print('here')
            cur_node=cur_node.next
            rev_node=ListNode(val=cur_node.val)
            rev_node.next=prev_node
            prev_node=rev_node
        # print(head)
        # print(rev_node)
        while head:
            if head.val==rev_node.val:
                # print(head.val)
                # print(rev_node.val)
                head=head.next
                rev_node=rev_node.next
            else:
                return False
        return True
#%% Use fast and slow to find the middle and reverse simultaneously, then compare the reversed linked list and the latter linked list.
class Solution:
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev           
                       
            