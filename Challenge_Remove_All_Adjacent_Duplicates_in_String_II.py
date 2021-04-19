#TLE answer
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        check=[]
        for i in range(len(s)):
            stack.append(s[i])
            check=stack[-k:]
            while len(check)==k and len(set(check))==1:
                stack=stack[:-k]
                check=stack[-k:]
        return(''.join(stack))
#%% Still TLE
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        check=[]
        for i in range(len(s)):
            stack.append(s[i])
            check=stack[-k:]
            if len(check)==k and len(set(check))==1:
            # if len(check)==k and all(element == check[0] for element in check):#=>確實也TLE 不過塞了一個for感覺很合理
                stack=stack[:-k]
        return(''.join(stack))
     
#%% Accepted solution
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        ans=''
        for i in range(len(s)):
            if stack and s[i]==stack[-1][0]:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([s[i],1])
        for i in stack:
            ans+=i[0]*i[1]
        return(ans)
#%% Fast solution
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        remove = []
        ## Generating possible duplicates
        for ch in set(s):
            remove.append(ch*k)
            
        old,new = s,s
        while True:
            for candidate in remove:
                new = new.replace(candidate,"")
            if len(old) == len(new):
                break
            old = new        
        return old
#%% equal to the solution above
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        
        dup = [char*k for char in set(s)]
        
        oldlen = -1
        while oldlen!=len(s):
            oldlen = len(s)
            for comb in dup:
                s = s.replace(comb,"")
        return s