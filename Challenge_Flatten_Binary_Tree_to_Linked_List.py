# My solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        def preorder(node,ls):
            ls.append(node.val)
            if node.left:
                preorder(node.left,ls)
            if node.right:
                preorder(node.right,ls)
        ls=[] 
        preorder(root,ls)

        rec=TreeNode(left=None,right=root)
        rec=rec.right
        for i in range(1,len(ls)):
            rec.left=None
            rec.right=TreeNode(val=ls[i])
            rec=rec.right 
#%% Other solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:  # 避免 empty tree
            return
        
        self.flatten(root.left)  # 把 left subtree 攤平
        self.flatten(root.right)  # 把 right subtree 攤平
        
        l = root.left  # l 為 left subtree
        r = root.right  # r 為 right subtree
        
        root.right = l  # 將 left subtree 接至 root 右邊
        root.left = None  # 將 root 左邊指向 None
        
        while root.right:  # 找到右邊的 leaf (也就是原 left subtree 的 leaf)
            root = root.right
        root.right = r  # 將原 right subtree 接至原 left subtree 之 leaf
#%% Other solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack=[root]
        while stack:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            cur.left=None
            cur.right=stack[-1] if stack else None
#%%
def __init__(self):
    self.prev = None
    
def flatten(self, root):
    if not root:
        return None
    self.flatten(root.right)
    self.flatten(root.left)
    
    root.right = self.prev
    root.left = None
    self.prev = root
#%%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                self.flatten(cur.left)
                left_tail = cur.left
                while left_tail.right:
                    left_tail = left_tail.right
                old_right = cur.right
                cur.right = cur.left
                cur.left = None
                left_tail.right = old_right
                left_tail.left = None
                cur = old_right
            else:
                cur = cur.right