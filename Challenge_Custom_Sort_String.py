# My solution
class Solution:
    def customSortString(self, order: str, str: str) -> str:    
        ans=""
        dic_s = collections.Counter(str)
        ls=list(dic_s.keys())
        for i in order:
            ans+=i*dic_s[i]
            if i in ls:
                ls.remove(i) 
        for i in ls:
            ans+=i*dic_s[i]
        return(ans)

#%% Revised my solution
class Solution:
    def customSortString(self, order: str, str: str) -> str:    
        ans=""
        dic_s = collections.Counter(str)
        ls=set(str)
        for i in order:
            ans+=i*dic_s[i]
            if i in ls:
                ls.remove(i) 
        for i in ls:
            ans+=i*dic_s[i]
        return(ans)
#%% Other solution
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        counter = collections.Counter(T)
        res = []
        for i in S:
            if i in counter:
                res.append(i*counter[i])
                counter.pop(i)
        for i, v in counter.items():
            res.append(i*v)
        return ''.join(res)

