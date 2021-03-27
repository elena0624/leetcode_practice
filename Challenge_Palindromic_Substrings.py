class Solution: # modify my longest palindromic substring answer, but not fast enough
    def countSubstrings(self, s: str) -> int:
        ans = 0
        odd_idx = [*range(len(s))] # or list(range(len(s)) # 所有都是 # 最新
        odd_idx_new = odd_idx.copy()# 當前
        ans+=len(odd_idx_new)

        str_len = 2
        even_idx = []
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                even_idx.append(i)
        even_idx_new = even_idx.copy()
        ans+=len(even_idx_new)

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
                ans+=len(odd_idx_new)
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
                ans+=len(even_idx_new)
            # 如果都沒有新的了
            if (not(odd_idx_new) and not(even_idx_new)):
                break
        
        return(ans)
#%% brilliant solution!!
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        i = 0
        while i < len(s):
            l=i
            r=i
            
            consecutives = 1;
            while r<len(s)-1 and s[r]==s[r+1]:
                consecutives+=1;
                r+=1;
                
            count+= consecutives*(consecutives + 1)//2
            i = r+1;

            while l>0 and r<len(s) -1 and s[r+1]==s[l-1]:
                r+=1
                l-=1
                count+=1
        return count