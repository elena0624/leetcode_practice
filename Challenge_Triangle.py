# My solution
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==1:
            return(triangle[0][0])

        for i in range(len(triangle)-2,-1,-1):
            cur_stack=[]
            if i==len(triangle)-2:
                last_stack=triangle[-1]
            for j in range(len(triangle[i])):
                cur_stack.append(triangle[i][j]+min(last_stack[j],last_stack[j+1]))
            last_stack=cur_stack
        return(cur_stack[0])
#%% Others solution
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for x in reversed(range(len(triangle) - 1)):
            for y in range(len(triangle[x])):
                triangle[x][y] += min(triangle[x + 1][y], triangle[x + 1][y + 1])
        
        return triangle[0][0]
#%%
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # bottim-up method
        res=triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                res[j]=triangle[i][j]+min(res[j],res[j+1])
        return res[0]
#%% Try to revised
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-1],[2,3],[1,-1,-3]]

last_stack=triangle[-1]
for i in range(len(triangle)-2,-1,-1):
    for j in range(len(triangle[i])):
        last_stack[j]=triangle[i][j]+min(last_stack[j],last_stack[j+1])
    print(last_stack)
print(last_stack[0])
