# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def visit(cur_root):
            if cur_root==None:
                return
            ans_list.append(cur_root.val)
            visit(cur_root.left)
            visit(cur_root.right)
        ans_list=[]
        cur_root=root
        visit(cur_root)
        return ans_list
#%% iterative solution
class Solution:
    def preorderTraversal(self, root):
            res, stack = [], []
            while root or stack:
                if root:
                    res += root.val,
                    stack += root.right, root.left,
                root = stack.pop()
            return res