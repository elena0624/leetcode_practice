class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        violate = False # 紀錄之前是否已有改過一個
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:# 如果發生deacreasing
                if violate:# 如果之前已改過一個
                    return(False)
                else:
                    if i==len(nums)-1:# 如果已經遍歷到最後可直接return了
                        return(True)
                    elif i>1 and nums[i+1]<nums[i-1] and nums[i]<nums[i-2]:
                    # i>1:如果i==1是第一個那就註記改過就好 不用顧慮是波峰還波谷
                    # nums[i+1]<nums[i-1]: 如果再下一個值比前一個值還小 代表前一個值異常大 所以要把前一個值改成跟i這個值一樣
                    # nums[i]<nums[i-2]: 如果把前一個值nums[i-1]改成跟nums[i]一樣結果反而造成前一個值比前前個值還小那就不行
                        return(False)
                    violate=True
                # 忽略一個如果nums[i+1]>nums[i-1]: 如果再下一個值比前一個值還大
                # 代表是這個值異常小 所以要把這個值改成跟前一個值i-1一樣大
                # 那就繼續正常看就好 反正下一個值確定比前一個值大了
        return(True)
#%% Other solution
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        res = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                res += 1
                if i>0 and i<len(nums) - 2 and nums[i-1]>nums[i+1] and nums[i]>nums[i+2]:
                    return False
        return res < 2