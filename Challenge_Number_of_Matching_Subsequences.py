# My solution
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        s_dict = collections.defaultdict(list)
        for i in range(len(s)):
            s_dict[s[i]].append(i)
        ans=len(words)
        for i in words:# n
            a=-1
            for j in i: # n
                if s_dict[j]==[]:
                    ans-=1
                    break
                else:
                    exist=False
                    for k in s_dict[j]:# a
                        if k>a:
                            a=k
                            exist=True
                            break
                    if exist==False:
                        ans-=1
                        break

        return(ans)
#%% Fast solution
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        for i, c in Counter(words).items():
            indexj = 0
            for j in i:
                indexj = s.find(j, indexj) + 1
                if not indexj:
                    break
            else:
                count +=c
        return count
#%% Elegant solution
class Solution:
    def numMatchingSubseq(self, s, words):
        res = 0
        for w,c in Counter(words).items():
            i, match = 0, True
            for x in w:
                i = s.find(x,i) + 1
                if not i:
                    match = False
                    break
            if match:
                res += c
        return res