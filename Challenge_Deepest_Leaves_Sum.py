# Deepest Leaves Sum
# Definition for a binary tree node. # My solution
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        temp=[]
        def bfs(depth,cur):
            if cur.left or cur.right:
                if cur.left:
                    bfs(depth+1,cur.left)
                if cur.right:
                    bfs(depth+1,cur.right)
            else:
                temp.append([depth,cur.val])
        bfs(0,root)
        #print(temp)
        max_depth = max(a for a,b in temp)
        return sum(b for a,b in temp if a==max_depth)
#%% Others solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        stack = [root]
        while True:
            new_stack=[]
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            if not new_stack:
                break
            stack = new_stack
        return sum(node.val for node in stack)
#%%
    def deepestLeavesSum(self, root):
        q = [root]
        while q:
            pre, q = q, [child for p in q for child in [p.left, p.right] if child]
        return sum(node.val for node in pre)