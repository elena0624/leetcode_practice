class Solution: # fast!吧
    def longestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return(s)
        str_len = 1 
        odd_idx = [*range(len(s))] # or list(range(len(s)) # 所有都是 # 最新
        odd_idx_new = odd_idx.copy()# 當前

        str_len = 2
        even_idx = []
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                even_idx.append(i)
        even_idx_new = even_idx.copy()

        for str_len in range(3,(len(s)+1)):#從3開始因為其他前面先初始化過了
            if str_len%2 == 1:    # 奇數情形
                # 如果前一輪還有
                if odd_idx_new:
                    odd_idx = odd_idx_new.copy() # 直接拿掉也可以
                    odd_idx_new = []
                    for idx in odd_idx:
                        if idx-1<0:#太小了不行 下一個
                            continue
                        elif idx+str_len-2>len(s)-1:#太大了不行 這輪end
                            break
                        elif s[idx-1]==s[idx+str_len-2]:
                            odd_idx_new.append(idx-1)# idx 紀錄起始位置
            else: #偶數情形
                # 如果前一輪還有
                if even_idx_new:
                    even_idx = even_idx_new.copy() # 直接拿掉也可以
                    even_idx_new = []
                    for idx in even_idx:
                        if idx-1<0:#太小了不行 下一個
                            continue
                        elif idx+str_len-2>len(s)-1:#太大了不行 這輪end
                            break
                        elif s[idx-1]==s[idx+str_len-2]:
                            even_idx_new.append(idx-1)# i 紀錄起始位置
            # 如果都沒有新的了
            if (not(odd_idx_new) and not(even_idx_new)):
                str_len = str_len-2
                if str_len%2==1:
                    return( s[odd_idx[0]:odd_idx[0]+str_len])
                else:
                    return( s[even_idx[0]:even_idx[0]+str_len])
        # 如果執行到最後odd或even的new裡還有東西=>完全相等的情況被排除了，所以是n-1裡面有東西
        str_len -= 1
        if str_len%2==1:
            return( s[odd_idx_new[0]:odd_idx_new[0]+str_len])
        else:
            return( s[even_idx_new[0]:even_idx_new[0]+str_len])
#%% 3/28 reference from palindromic substring brilliant solution NICE!!
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return(s)
        i=0
        all_long_len=1
        all_l=0
        while i<len(s):
            cur_long_len=1
            r=i
            l=i
            while (r<len(s)-1 and s[r]==s[r+1]):
                r+=1
                cur_long_len+=1
            i=r+1
            while (l>0 and r<len(s)-1 and s[l-1]==s[r+1]):
                l-=1
                r+=1
                cur_long_len+=2
            if cur_long_len>all_long_len:
                all_long_len=cur_long_len
                all_l=l

        return(s[all_l:all_l+all_long_len])