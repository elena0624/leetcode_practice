# My solution (slow)
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = sorted(words,key = lambda x:len(x), reverse=True)

        max_len=0

        for i in range(len(words)):
            a_len=len(words[i])
            a_set=set(words[i])
            if a_len*a_len<=max_len:# 稍微剪枝
                break
            for j in range(i+1,len(words)):
                b_len=len(words[j])
                if b_len<=(max_len//a_len):# 稍微剪枝
                    break
                if a_set.isdisjoint(set(words[j])):
                    max_len=max(max_len,a_len*b_len)
        return(max_len)
#%% 10X Fast solution
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = {sum(1 << (ord(c) - 97) for c in set(w)): len(w) for w in sorted(words, key=len)}
        return max([d[k] * d[K] for k, K in itertools.combinations(d.keys(), 2) if not K & k] or [0])
#%%
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97))
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])
