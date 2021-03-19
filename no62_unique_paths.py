class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # solution1
        maze = [[0],[1]*(n+1)] # 列存往下走m,行存往右走n
        for i in range(2,m+1):
            maze.append([0,1])
            for j in range(2,n+1):
                maze[i].append(maze[i-1][j] + maze[i][j-1])
        return(maze[m][n])