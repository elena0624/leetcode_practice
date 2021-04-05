# Stupid solution. TLE
class Solution:
def isIdealPermutation(self, A: List[int]) -> bool:
    for i in range(len(A)):
        for j in range(i+2,len(A)):
            if A[i]>A[j]:
                return(False)
    return(True)
#%%
# Acceptable solution
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        lc_min=5000
        for i in range(len(A)-1,1,-1):#
            if A[i]<lc_min:
                lc_min = A[i]

            if A[i-2]>lc_min:
                return(False)
        return(True)
#%% Brilliant solution
class Solution:
def isIdealPermutation(self, A: List[int]) -> bool:
    for i in range(len(A)):
        if A[i]<(i-1) or A[i]>(i+1):#same to=> abs(A[i]-i)>=2
            return(False)
    return(True)