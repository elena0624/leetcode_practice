class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        row_sum = [[0]*(n+1) for i in range(m)]
        # compute row presum
        for i in range(m):
            row_sum[i][1]=matrix[i][0]
            for j in range(2,n+1):
                row_sum[i][j]=matrix[i][j-1]+row_sum[i][j-1]

        ans=0
        # select each 2 columns and turns to problem 560
        for i in range(n):
            for j in range(i+1,n+1):
                sub_matrix_sum = collections.defaultdict(int)
                sub_matrix_sum[0]=1
                cur_sum=0
                for k in range(m):
                    cur_sum+=(row_sum[k][j]-row_sum[k][i])
                    ans+= sub_matrix_sum[cur_sum-target]
                    sub_matrix_sum[cur_sum]+=1
        return(ans)

#%% Others' Solution
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ps = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ps[i+1][j] = ps[i][j]+matrix[i][j]
        res = 0
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)+1):
                col_sum = {0:1}
                cur_sum = 0
                for k in range(len(matrix[0])):
                    cur_sum += ps[j][k] - ps[i][k]
                    if cur_sum - target in col_sum:
                        res += col_sum[cur_sum - target]
                    if cur_sum in col_sum:
                        col_sum[cur_sum] += 1
                    else:
                        col_sum[cur_sum] = 1
        return res