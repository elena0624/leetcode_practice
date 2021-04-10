class Solution: # DFS Brute force. Will get TLE if didn't use @lru_cache(None)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(depth,i,j):
            if not searchNeighbor(i,j):
                temp[i][j]=max(temp[i][j],depth)
        #        if depth>max_depth:
        #            max_depth=depth
                return
            for a,b in searchNeighbor(i,j):
                # print(a,b)
                if depth<temp[i][j]:##如果比較少的應該不用走了?
                    return
                dfs(depth+1,a,b)
                temp[i][j]=max(temp[i][j],depth)

        # 從每一個點作為起點開始走
        @lru_cache(None)
        def searchNeighbor(i,j):
            available=[]
            # 上
            if i-1>=0:
                if matrix[i-1][j]>matrix[i][j]:
                    available.append((i-1,j))
            # 下
            if (i+1)<=(m-1):
                if matrix[i+1][j]>matrix[i][j]:
                    available.append((i+1,j))
            # 左
            if (j-1)>=0:
                if matrix[i][j-1]>matrix[i][j]:
                    available.append((i,j-1))
            # 右
            if (j+1)<=(n-1):
                if matrix[i][j+1]>matrix[i][j]:
                    available.append((i,j+1))
            return available

        # 從每一個點作為起點開始走
        @lru_cache(None)
        def checkNeighbor(i,j):
            available=[]
            # 上
            if i-1>=0:
                if matrix[i-1][j]<matrix[i][j]:
                    available.append((i-1,j))
            # 下
            if (i+1)<=(m-1):
                if matrix[i+1][j]<matrix[i][j]:
                    available.append((i+1,j))
            # 左
            if (j-1)>=0:
                if matrix[i][j-1]<matrix[i][j]:
                    available.append((i,j-1))
            # 右
            if (j+1)<=(n-1):
                if matrix[i][j+1]<matrix[i][j]:
                    available.append((i,j+1))
            return available
        m=len(matrix)
        n=len(matrix[0])
        temp=[[1]*n for i in range(m)]
        # max_depth=0
        for i in range(m):
            for j in range(n):
                if not checkNeighbor(i,j):# 代表周圍沒有更小
                    dfs(1,i,j)
        return((max(max(x) for x in temp)))
#%% Revised solution using dp to save the longest path from each point
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        @lru_cache(None)
        def dfs(i,j):
            if not searchNeighbor(i,j):
                temp[i][j]=1
                return 1
            if temp[i][j]>0:
                return temp[i][j]
            else:
                temp[i][j]=max(dfs(a,b)+1 for a,b in searchNeighbor(i,j))
        #    print(temp)
            return temp[i][j]
        @lru_cache(None)
        def searchNeighbor(i,j):
            available=[]
            # 上
            if i-1>=0:
                if matrix[i-1][j]>matrix[i][j]:
                    available.append((i-1,j))
            # 下
            if (i+1)<=(m-1):
                if matrix[i+1][j]>matrix[i][j]:
                    available.append((i+1,j))
            # 左
            if (j-1)>=0:
                if matrix[i][j-1]>matrix[i][j]:
                    available.append((i,j-1))
            # 右
            if (j+1)<=(n-1):
                if matrix[i][j+1]>matrix[i][j]:
                    available.append((i,j+1))
            return available

        temp=[[0]*n for i in range(m)]
        max_depth=0
        for i in range(m):
            for j in range(n):
                dfs(i,j)
        return((max(max(x) for x in temp)))
#%% Other ones fast solution
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # corner case
        if not matrix or not matrix[0]:
            return 0

        # initilization
        M, N = len(matrix), len(matrix[0]) # length, width
        dp = [[0]*N for i in range(M)] # 2-D matrix for store the number of steps

        # dfs function
        def dfs(i, j):
            if not dp[i][j]: # if this position is not visited
                val = matrix[i][j]
                # search four directions to find out the decreasing path
                # up
                if i and val > matrix[i-1][j]:
                    up = dfs(i-1, j)
                else:
                    up = 0
                # down
                if i < M-1 and val > matrix[i+1][j]:
                    down = dfs(i+1, j)
                else:
                    down = 0
                # left
                if j and val > matrix[i][j-1]:
                    left = dfs(i, j-1)
                else:
                    left = 0
                # right
                if j < N-1 and val > matrix[i][j+1]:
                    right = dfs(i, j+1)
                else:
                    right = 0
                # "walk" to the target neighbor and accumulate the number of steps
                dp[i][j] = 1 + max(up, down, left, right)
            return dp[i][j]

        res_path = []
        for x in range(M): # search the grid by dfs
            for y in range(N):
                res_path.append(dfs(x, y))

        return max(res_path)
#%% My solution refered to others
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # corner case

        m=len(matrix)
        n=len(matrix[0])
        @lru_cache(None)
        def dfs(i,j):
            if temp[i][j]>0:
                return temp[i][j]

            # available=[]
            # 上
            if i-1>=0 and matrix[i-1][j]>matrix[i][j]:
                up=dfs(i-1,j)+1
            else:
                up=1
            # 下
            if (i+1)<=(m-1) and matrix[i+1][j]>matrix[i][j]:
                down =dfs(i+1,j)+1
            else:
                down=1
            # 左
            if (j-1)>=0 and matrix[i][j-1]>matrix[i][j]:
                left=dfs(i,j-1)+1
            else:
                left=1
            # 右
            if (j+1)<=(n-1) and matrix[i][j+1]>matrix[i][j]:
                right = dfs(i,j+1)+1
            else:
                right=1
            temp[i][j]=max(up,down,left,right)
        #    print(temp)
            return temp[i][j]

        temp=[[0]*n for i in range(m)]
        max_depth=0
        for i in range(m):
            for j in range(n):
                max_depth=max(max_depth,dfs(i,j))
        return(max_depth)
