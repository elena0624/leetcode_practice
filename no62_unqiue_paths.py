# solution1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       
        maze = [[0],[1]*(n+1)] # 列存往下走m,行存往右走n
        for i in range(2,m+1):
            maze.append([0,1])
            for j in range(2,n+1):
                maze[i].append(maze[i-1][j] + maze[i][j-1])
        return(maze[m][n])
#%%
# solution2
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return(1)
        else:
        # 最新一列
            n_row = [1]*(n-1) # 只差在這邊!!!!
            for i in range(0,m-1):
                # 目前的那個
                target = 1 # 第一個都是1
                for j in range(0,n-1):
                    target = n_row[j] + target
                    n_row[j] = target
            return(target)
#%%
# solution3
class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        n_row = [1]*n # 第一列都是1 (index=0~n-1)
        for _ in range(1,m): # 有幾列其實不會用到,只是要執行那麼多次而已
            for j in range(1,n):
                n_row[j] = n_row[j] + n_row[j-1] # n_row[0]永遠是1不會被更新到
        return(n_row[-1])