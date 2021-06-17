# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 18:23:46 2021

@author: ppj
"""

nums = [2, 1, 4, 3]
left = 2
right = 3

nums = [73,55,36,5,55,14,9,7,72,52]
left = 32
right= 69

#nums=[16,69,88,85,79,87,37,33,39,34]
#left=55
#right=57

#nums=[876,880,482,260,132,421,732,703,795,420,871,445,400,291,358,589,617,202,755,810,227,813,549,791,418,528,835,401,526,584,873,662,13,314,988,101,299,816,833,224,160,852,179,769,646,558,661,808,651,982,878,918,406,551,467,87,139,387,16,531,307,389,939,551,613,36,528,460,404,314,66,111,458,531,944,461,951,419,82,896,467,353,704,905,705,760,61,422,395,298,127,516,153,299,801,341,668,598,98,241]
#left=658
#right=719


cur=0
ans=0
low=0
#cur_max=0
cur_max=False
for i in range(len(nums)):
    print(nums[i])
    # 直接爆開
    if nums[i]>right:
        cur=0
        cur_max=False
#        cur_max=0
    # 符合標準
    elif nums[i]>=left and nums[i]<=right:
        # 連續的
        low=0
        ans+=1
        ans+=cur
        cur+=1
        cur_max=True
#        cur_max=max(cur_max,nums[i])
    # 不符標準，但前面有cur_max可以靠
    elif nums[i]<left:
        if cur_max:
            ans+=cur
            ans-=low
        cur+=1
        low+=1
    print('ans',ans,'cur',cur,'curmax',cur_max)
# 最後一個若符合也要算
#ans+=((cur+1)*cur)//2
print(ans)