class Solution:
    def minOperations(self, n: int) -> int:
        if n%2==1:
            ans= (((n-1)//2)*2)*(n+1)//2//2
        else:
            ans=(1+(n//2)*2-1)*n//2//2
        return(ans)
#%%
class Solution:
    def minOperations(self, n: int) -> int:
        return (n*n)//4