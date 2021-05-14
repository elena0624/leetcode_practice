# My solution
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def possible_comb(s):
            s_ls = []
            if len(s)==1:
                return [s]
            if s.count('0')==len(s) or s[0]==s[-1]=='0':
                return False
            if s[-1]=='0':
                return [s]
            if s[0]=='0':
                return [s[0]+'.'+s[1:]]
            else:
                for i in range(len(s)-1):
                    s_ls.append(s[:i+1]+'.'+s[i+1:])
                s_ls.append(s)
                return s_ls
        ans_ls=[]
        for i in range(2,2+len(s[2:-1])):
            s1 = possible_comb(s[1:i])
            s2 = possible_comb(s[i:-1])
            if s1 and s2:
                ans_ls.extend(['('+a+', '+b+')' for a in s1 for b in s2])
        return(ans_ls)
