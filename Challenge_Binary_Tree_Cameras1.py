# -*- coding: utf-8 -*-
"""
Created on Mon May 17 14:15:08 2021

@author: ppj
"""
#%% Failed code1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=0
    def minCameraCover(self, root: TreeNode) -> int:
        if root.val==0: #自己還沒被監控,要決定是要放在自己身上還是子身上;決定關鍵:
            # 有沒有兒子 沒有就放自己
            if not root.left and not root.right:
                #print('沒而 放自己')
                self.ans+=1
                root.val=2
            # 只有一邊兒子 那優先放另一邊兒子
            elif root.left and not root.right:
                self.ans+=1
                root.val=1
                root.left.val=2
                if root.left.left:
                    root.left.left.val=1
                if root.left.right:
                    root.left.right.val=1
            elif root.right and not root.left:
                self.ans+=1
                root.val=1
                root.right.val=2
                if root.right.left:
                    root.right.left.val=1
                if root.right.right:
                    root.right.right.val=1
            # 兩邊都有兒子
            else:
                # 任一邊絕後的話放自己
                #print(root.left)
                #print(root.right)
                if (not root.left.left and not root.left.right) or (not root.right.left and not root.right.right):
                    self.ans+=1
                    root.val=2
                    root.left.val=1
                    root.right.val=1
                    
                # 兩邊都有後，放沒孫子的兒子
                # 若左邊沒孫放左子
                elif (root.left.left and not root.left.left.left and not root.left.left.right and not root.left.right) or (root.left.right and not root.left.right.left and not root.left.right.right and not root.left.left) or (root.left.left and not root.left.left.left and not root.left.left.right and root.left.right and not root.left.right.left and not root.left.right.right):
                    self.ans+=1
                    root.val=1
                    root.left.val=2
                    if root.left.left:
                        root.left.left.val=1
                    if root.left.right:
                        root.left.right.val=1
                #  右邊沒孫子放右子 
                elif (root.right.left and not root.right.left.left and not root.right.left.right and not root.right.right) or (root.right.right and not root.right.right.left and not root.right.right.right and not root.right.left) or (root.right.left and not root.right.left.left and not root.right.left.right and root.right.right and not root.right.right.left and not root.right.right.right):
                    self.ans+=1
                    root.val=1
                    root.right.val=2
                    if root.right.left:
                        root.right.left.val=1
                    if root.right.right:
                        root.right.right.val=1
                # 都有孫就挑一個放
                else:
                    self.ans+=1
                    root.val=1
                    root.left.val=2
                    if root.left.left:
                        root.left.left.val=1
                    if root.left.right:
                        root.left.right.val=1                    


        #elif root.val==1: #雖然自己被監控過了(非放置) 但有種情況自己還是要上: 當兩邊都有兒子且沒孫子的時候
        elif root.val==1: #雖然自己被監控過了(非放置) 但有種情況自己還是要上: 當兩邊都有兒子且任一邊沒孫子的時候
            #if root.left and not root.left.left and not root.left.right and root.right and not root.right.left and not root.right.right:
            if root.left and root.right and ((not root.left.left and not root.left.right) or (not root.right.left and not root.right.right)):
                self.ans+=1
                root.val=2
                root.left.val=1
                root.right.val=1
        if root.left:
            self.minCameraCover(root.left)
        if root.right:
            self.minCameraCover(root.right)
        #print('next')
        return self.ans
#%% Failed code2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=0
    def minCameraCover(self, root: TreeNode) -> int:
        def is_leaf(node):
            if (not node.left or (node.left and node.left.val==2)) and (not node.right or (node.right and node.right.val==2)):
                #node.val=1
                return True
            else:
                return False
            
        def is_leafParent(node):
            if node.left and is_leaf(node.left):
                #self.ans+=1
                #node.val=1# camera
                return True
            if node.right and is_leaf(node.right):
                #self.ans+=1
                #node.val=1# camera
                return True
            else:
                return False
        def set_camera(node):
            ######下面的先用好再回來用自己
            if node.left:
                set_camera(node.left)
            if node.right:
                set_camera(node.right)
            
            #print(node)
            if node.val==0: #not covered
                if node.left and node.left.val==1:
                    node.val=2 # covered but not camera
                elif node.right and node.right.val==1:
                    node.val=2 # covered but not camera
                else: # 真的沒被cover到
                    if is_leafParent(node):
                        self.ans+=1
                        node.val=1 # set camera
                        if node.left:
                            node.left.val=2
                        if node.right:
                            node.right.val=2
                   # else: # 不是葉祖父 那就要往下繼續check
        #if not root.left and not root.right:
            
           # return 1
        set_camera(root)
        if root.val==0
            self.ans+=1
        return self.ans
#%% 修改以上code後accept
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
            if (not node.left or (node.left and node.left.val==2)) and (not node.right or (node.right and node.right.val==2)):
                node.val=3
                return True
            else:
                return False

        def is_leafParent(node):
            if node.left and node.left.val==3:
                #self.ans+=1
                #node.val=1# camera
                return True
            if node.right and node.right.val==3:
                #self.ans+=1
                #node.val=1# camera
                return True
            else:
                return False
        def set_camera(node):
            ######下面的先用好再回來用自己
            if node.left:
                set_camera(node.left)
            if node.right:
                set_camera(node.right)

            #print(node)
            #if node.val==0: #not covered=> 不用管當下這個CO步COVER
                #多加一個直接判斷是自己就是葉的情形
            if is_leaf(node):
                return
            # 看兒子如果有涉過cmaera自己就要改掉                
            if node.left and node.left.val==1:
                node.val=2 # covered but not camera
            if node.right and node.right.val==1:
                node.val=2 # covered but not camera
            # 是不是葉 如果是葉就要設CAMERA
            if is_leafParent(node):
                self.ans+=1
                node.val=1 # set camera
                if node.left:#其實兒子也不用特別去改了啦
                    node.left.val=2
                if node.right:
                    node.right.val=2
                #else: # 真的沒被cover到

                   # else: # 不是葉祖父 那就要往下繼續check
        #if not root.left and not root.right:

           # return 1
        set_camera(root)
        #print(root)
        if root.val!=1 and root.val!=2:
            self.ans+=1
        return self.ans
#%% Slightly simplize
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
#%%
        
        