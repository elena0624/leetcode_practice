#%% 1805 Number of Different Integers in a String
class Solution: #My solution
    def numDifferentIntegers(self, word: str) -> int:
        word2= ''
        for i in range (len(word)):
            if word[i] in string.ascii_lowercase:
                word2+=' '
            else:
                word2+=word[i]
        #print(int())
        return(len(set(list(map(int,word2.split())))))
#%% My solution after revision
from string import digits
class Solution: 
    def numDifferentIntegers(self, word: str) -> int:
        ans = set()
        i=0
        while i < (len(word)):
            if word[i].isdigit():
                l=i
                while l <len(word) and word[l].isdigit():
                    l+=1
                ans.add(int(word[i:l]))
                i=l+1
            else:
                i+=1
        return(len(ans))
#%%  Other ones solutions1
class Solution(object):
    def numDifferentIntegers(self, word):
        seen = set()
        for k,grp in groupby(word, key=lambda c: c.isdigit()):
            if k:
                s = "".join(grp)
                seen.add(int(s))
        return len(seen)
#%%  Other ones solutions2
from string import digits
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ret = set()
        i = 0
        while i < len(word):
          if word[i] not in digits:
            i += 1
            continue
          j = i
          while j < len(word) and word[j] in digits:
            j += 1
          ret.add(int(word[i:j]))
          i = j
        return len(ret)
#%% 1806 Minimum Number of Operations to Reinitialize a Permutation
class Solution: # My solution
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        arr = perm.copy()
        s=1
        equal_list = True
        for i in range(n):
            if i % 2 == 0:
                arr[i] = perm[int(i / 2)]
            else:
                arr[i] = perm[int(n / 2 + (i - 1) / 2)]
            if arr[i] != perm[i]:
                equal_list = False
        if equal_list:
            return(s)

        new_arr = arr.copy()

        while True:
            s+=1
            equal_list = True
            for i in range(n):
                if i % 2 == 0:
                    new_arr[i] = arr[int(i / 2)]
                else:
                    new_arr[i] = arr[int(n / 2 + (i - 1) / 2)]
                if new_arr[i] != perm[i]:
                    equal_list = False
            if equal_list:
                return(s)
            arr = new_arr.copy()
#%% My solution after revision
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        arr = perm.copy()
        s=0
        while True:
            s+=1
            arr = [arr[i//2] if i%2==0 else arr[n//2 + (i-1)//2] for i in range(n)]
            if arr == perm:
                return(s)
#%%  Other ones solutions1
class Solution(object):
    def reinitializePermutation(self, n):
        A = range(n)
        ans = 0
        while True:
            ans += 1
            A = [A[i >> 1] if i % 2 == 0 else A[((i-1) // 2) + n // 2] for i in xrange(n)]
            if all(i==A[i] for i in xrange(n)): break
        return ans
#%%  Other ones solutions2
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        orig = list(perm)
        ops = 0
        while True:
            ops += 1
            perm = [perm[i // 2] if i % 2 == 0 else perm[n // 2 + (i - 1) // 2] for i in range(n)]
            if perm == orig:
                return ops
        return 0
#%% 1807 Evaluate the Bracket Pairs of a String
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_dict = {}
        for i in range(len(knowledge)):
            knowledge_dict.setdefault(knowledge[i][0],knowledge[i][1])
        c_loc1=[]
        c_loc2=[]
        for i, c in enumerate(s):
                if c == '(':
                    c_loc1.append(i)
                elif c == ')':
                    c_loc2.append(i)
        if not c_loc1:
            return(s)
        temp_list = list(zip(c_loc1,c_loc2))
        temp_list = list(map(list, temp_list))
        s2 = s
        s2 = s[0:temp_list[0][0]] 
        for i in range(len(temp_list)-1):
            s2+=knowledge_dict.get(s[temp_list[i][0]+1:temp_list[i][1]], "?")
            s2+=s[temp_list[i][1]+1:temp_list[i+1][0]]
        s2+=knowledge_dict.get(s[temp_list[-1][0]+1:temp_list[-1][1]], "?")
        s2+=s[temp_list[-1][1]+1:] 
        return(s2)
#%% My solution after revision
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_dict = {}
        for k,v in knowledge:
            knowledge_dict[k]=v
        i=0
        ans=''
        while i<len(s):
            if s[i]=='(':
                l=i+1
                while l<len(s) and s[l]!=')':
                    l+=1
                ans+=knowledge_dict.get(s[i+1:l], "?")
                i=l+1
            else:
                ans+=s[i]
                i+=1
        return(ans)
#%%  Other ones solutions1
class Solution(object):
    def evaluate(self, s, knowledge):
        M = {}
        for k,v in knowledge: M[k] = v
        
        ans = []
        i = 0
        while i < len(s):
            c = s[i]
            if c != '(':
                ans.append(c)
                i += 1
                continue
            else:
                j = i
                while s[j] != ')':
                    j += 1
                inner = s[i+1:j]
                if inner in M:
                    ans.append(M[inner])
                else:
                    ans.append('?')
                i = j + 1
        
        return "".join(ans)
#%%  Other ones solutions2
class Solution(object):
    def evaluate(self, s, mp0):
        n = len(s)
        res = ''
        i = 0
        mp = dict()
        for x in mp0:
            mp[x[0]] = x[1]
        while i < n:
            if s[i]=='(':
                j = i+1
                while j < n and s[j] != ')':
                    j+=1
                tmp = s[i+1:j]
                if tmp in mp:
                    res += mp[tmp]
                else:
                    res += '?'
                i = j + 1
            else:
                res += s[i]
                i+=1
        return res
        
#%% 1808 Maximize Number of Nice Divisors
class Solution: # TLE, mod error
    def maxNiceDivisors(self, primeFactors: int) -> int:
        mod = 10**9+7
        if primeFactors ==1:
            return(1)
        elif primeFactors%3==0:
            return(3**(primeFactors//3)%mod)
        elif primeFactors%3==1:
            num3=(primeFactors-1)//3-1# 3n+1要拆成3m+2k=>3(n-1)+4=3(n-1)+2x2
            num2=2
            return((3**num3)*4%mod)
        elif primeFactors%3==2:
            num3=(primeFactors-2)//3# 3n+1要拆成3m+2k=>3(n-1)+4=3(n-1)+2x2
            return((3**num3)*2%mod)
#%% My solution after revision
class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        mod = 10**9+7
        if primeFactors ==1:
            return(1)
        elif primeFactors%3==0:
            return(pow(3,(primeFactors//3),mod))
        elif primeFactors%3==1:
            num3=(primeFactors-1)//3-1# 3n+1要拆成3m+2k=>3(n-1)+4=3(n-1)+2x2
            num2=2
            return((pow(3,num3,mod)*4)%mod)
        elif primeFactors%3==2:
            num3=(primeFactors-2)//3# 3n+1要拆成3m+2k=>3(n-1)+4=3(n-1)+2x2
            return((pow(3,num3,mod)*2)%mod)
#%%  Other ones solutions1
class Solution(object):
    def maxNiceDivisors(self, n):
        MOD = 10 ** 9 + 7
        if n <=4: return n
        if n==5: return 6
        if n==6: return 9
        if n==7: return 12

        q,r = divmod(n-4, 3)
        return pow(3, q, MOD) * self.maxNiceDivisors(r+4) % MOD
#%%  Other ones solutions2
MOD = 1000000007

class Solution:
    def maxNiceDivisors(self, n: int) -> int:
        if n <= 3:
            return n
        if n % 3 == 1:
            return 4 * pow(3, (n - 4) // 3, MOD) % MOD
        elif n % 3 == 2:
            return 2 * pow(3, n // 3, MOD) % MOD
        else:
            return pow(3, n // 3, MOD)