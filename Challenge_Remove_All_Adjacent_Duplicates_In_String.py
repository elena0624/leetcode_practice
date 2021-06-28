#%% O(n)solution using stack
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if stack and stack[-1]==s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return(''.join(stack))
#%% using replace. The latter one is far more faster
class Solution:
    def removeDuplicates(self, s: str) -> str:
        re=set([i*2 for i in s])

        prev=-1
        while prev!=len(s):
            prev=len(s)
            for r in re:
                #print(r)
                s=s.replace(r,'')
        return(s)
#%% Fast answer.
from string import ascii_lowercase
class Solution:
    def removeDuplicates(self, s: str) -> str:
        duplicates = [2*ch for ch in ascii_lowercase]
        prev_length = -1
        while prev_length!=len(s):
            prev_length=len(s)
            for d in duplicates:
                s=s.replace(d, '')
        return s