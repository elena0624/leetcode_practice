# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        a_ls = []
        while head:
            a_ls.append(head.val)
            head=head.next
        def to_tree(ls):
            if len(ls)==0:
                return None
            elif len(ls)==1:
                return TreeNode(val=ls[0])
            else:
                ls_n=len(ls)
                root=TreeNode(val=ls[(ls_n)//2])
                root.left=to_tree(ls[:(ls_n)//2])
                root.right=to_tree(ls[(ls_n)//2+1:])
            return root
        root = to_tree(a_ls)
        return root
#%% Fastest solution
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)
        if head.next.next == None:
            return TreeNode(head.next.val, left=TreeNode(head.val))
        if head.next.next.next == None:
            return TreeNode(head.next.val, left=TreeNode(head.val), right=TreeNode(head.next.next.val))
        
        p0 = head# 快
        p1 = head# 慢
        p2 = None# 慢
        
        while p0!=None:
            p2 = p1
            if p0.next != None:
                p0 = p0.next
            p1 = p1.next
            p0 = p0.next
        
        p2.next = None# 用來改掉右子head的結尾 p1的next(納為啥不能用p1就好?=>因為p1的next要繼續指下去左子樹)
        # return p1. 因為p1會是中間點 當root 
        # 左子樹就是中點以左的
        # 右子樹就是中點下一個
        return TreeNode(p1.val, left = self.sortedListToBST(head), right = self.sortedListToBST(p1.next))
#%% Solution like above
class Solution:
    def sortedListToBST(self, head):
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        # here we get the middle point,
        # even case, like '1234', slow points to '2',
        # '3' is root, '12' belongs to left, '4' is right
        # odd case, like '12345', slow points to '2', '12'
        # belongs to left, '3' is root, '45' belongs to right
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # tmp points to root
        tmp = slow.next
        # cut down the left child
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root
#%% Practice
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head):
        # 可快速返回
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        if not head.next.next:
            return TreeNode(head.next.val,left=TreeNode(head.val))
        if not head.next.next.next:
            return TreeNode(head.next.val,left=TreeNode(head.val),right=TreeNode(head.next.next.val))
        # 開始快慢指針
        fast=slow=head
        while fast and fast.next:
            tmp=slow
            fast=fast.next.next
            slow=slow.next
        tmp.next=None
        
        
        
        # 此時slow是中點
        return TreeNode(slow.val,left=self.sortedListToBST(head),right=self.sortedListToBST(slow.next))
#%% Fast!
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head):
        # 可快速返回
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        if not head.next.next:
            return TreeNode(head.next.val,left=TreeNode(head.val))
        if not head.next.next.next:
            return TreeNode(head.next.val,left=TreeNode(head.val),right=TreeNode(head.next.next.val))
        # 開始快慢指針
        fast=slow=head
        while fast:
            tmp=slow
            if fast.next:
                fast=fast.next
            fast=fast.next
            slow=slow.next
        tmp.next=None
        
        
        
        # 此時slow是中點
        return TreeNode(slow.val,left=self.sortedListToBST(head),right=self.sortedListToBST(slow.next))