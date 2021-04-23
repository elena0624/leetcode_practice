# My slow solution
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i=0
        ans=0
        while (i+1)<len(s):
            if s[i]!=s[i+1]:
                ans+=1
                l=i
                r=i+1
                while l>0 and (r+1)<len(s) and s[l-1]==s[l] and s[r+1]==s[r]:
                    ans+=1
                    l-=1
                    r+=1
                i=r
            else:
                i+=1
        return(ans)
#%% Group by solution
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups=[1]
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                groups.append(1)
            else:
                groups[-1]+=1
        ans=0
        for i in range(len(groups)-1):
            ans+=min(groups[i],groups[i+1])
        return(ans)
#%% Group by brief solution
class Solution(object):
    def countBinarySubstrings(self, s):
        groups = [len(list(v)) for _, v in itertools.groupby(s)]
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))
#%% Linear
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev=0
        cur=1
        ans=0
        for i in range(1,len(s)):
            if s[i-1]!=s[i]:
                ans+=min(prev,cur)
                prev=cur
                cur=1
            else:
                cur+=1
        ans+=min(prev,cur)
        return(ans)
#%% Brief
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s=list(map(len,s.replace('01','0 1').replace('10','1 0').split()))

        return sum(min(a,b) for a,b in zip(s,s[1:]))