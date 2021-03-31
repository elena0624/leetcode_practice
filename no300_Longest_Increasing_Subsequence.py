# n^2 solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis=[1]*len(nums) # 紀錄該段最長lis是多少 最短是1(剛好全部倒敘的話就會是1)
        for i in range(1,len(nums)): # 檢查每一個位置
            max_lis=0
            for j in range(0,i): # 列出該位置之前的所有dp
                if nums[i]>nums[j]:# 所有前面比她小的 裡面找lis最大的
                    if lis[j]>max_lis:
                        max_lis=lis[j]
            lis[i]=max_lis+1
        return(max(lis))

#%% nlogn solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis_bound = [nums[0]]

        for i in range(1,len(nums)):
            if nums[i]>lis_bound[-1]:
                lis_bound.append(nums[i])
            elif nums[i]<lis_bound[0]:
                lis_bound[0]=nums[i]
            elif nums[i] in lis_bound:
                continue
            else:
                # 從lis_bound去找他所處的位置
                l=0
                r=len(lis_bound)-1
                while l<r:
                    m=(l+r)//2
                    if nums[i]>lis_bound[m]:# >m，因為找找比x大的，m也不用考慮了
                        l=m+1
                    else:#<m 因為要找比x大的,所以m也要考慮
                        r=m
                lis_bound[r]=nums[i]
        #print(lis_bound)
        return(len(lis_bound))
        