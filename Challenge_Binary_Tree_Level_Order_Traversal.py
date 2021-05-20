# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        stack=[]
        if root:
            stack.append(root)
        ans=[]
        while stack:
            n_stack=[]
            cur_lay=[]
            for i in stack:
                cur_lay.append(i.val)
                if i.left:
                    n_stack.append(i.left)
                if i.right:
                    n_stack.append(i.right)
            stack=n_stack
            ans.append(cur_lay)
        return ans
#%%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return ans