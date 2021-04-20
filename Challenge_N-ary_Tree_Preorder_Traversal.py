# Recursive solution
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans=[]
        def visit(node):
            ans.append(node.val)
            for i in node.children:
                visit(i)
            return
        if root:
            visit(root)
        else:
            return ans
        return ans
#%% Iterative
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans=[]
        stack=[]
        stack.append(root)
        while root and stack:
            cur=stack.pop()
            ans.append(cur.val)
            for i in range(len(cur.children),0,-1):
                stack.append(cur.children[i-1])                
        return ans
#%% Others' answer
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []
        
        L = [root.val]
        for c in root.children:
            if c:
                L += self.preorder(c)
                
        return L``

