# My answer (Not elegant)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.ans=0
            
        def is_leaf(node):
            # 判斷自己是不是葉
            if not node:
                return False
            if (not node.left or node.left.val==2) and (not node.right or node.right.val==2):
                return True
        def set_camera(node):
            ######下面的先用好再回來用自己
            if node.left:
                set_camera(node.left)
            if node.right:
                set_camera(node.right)
            
            # 更新自己的狀態
            if node.left and node.left.val==1:
                node.val=2 # covered but not camera
            if node.right and node.right.val==1:
                node.val=2 # covered but not camera
            # 檢查自己是否要裝camera=>要裝camera的條件 有是葉的兒子
            if is_leaf(node.left) or is_leaf(node.right):
                self.ans+=1
                node.val=1 # set camera
        set_camera(root)
        if root.val==0:
            self.ans+=1
        return self.ans
#%% elegant answer
 def minCameraCover(self, root):
        self.res = 0
        def dfs(root):
            if not root: return 2
            l, r = dfs(root.left), dfs(root.right)
            if l == 0 or r == 0:
                self.res += 1
                return 1
            return 2 if l == 1 or r == 1 else 0
        return (dfs(root) == 0) + self.res
#%% Official solution 1
class Solution(object):
    def minCameraCover(self, root):
        def solve(node):
            # 0: Strict ST; All nodes below this are covered, but not this one
            # 1: Normal ST; All nodes below and incl this are covered - no camera
            # 2: Placed camera; All nodes below this are covered, plus camera here

            if not node: return 0, 0, float('inf')
            L = solve(node.left)
            R = solve(node.right)

            dp0 = L[1] + R[1]#
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            dp2 = 1 + min(L) + min(R)

            return dp0, dp1, dp2

        return min(solve(root)[1:])
#%% Official solution2
class Solution(object):
    def minCameraCover(self, root):
        self.ans = 0
        covered = {None}

        def dfs(node, par = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                # 列出所有要裝camera的情形=>沒被cover,沒父,某子沒被cover
                if (par is None and node not in covered or
                        node.left not in covered or node.right not in covered):
                    self.ans += 1
                    covered.update({node, par, node.left, node.right})

        dfs(root)
        return self.ans
