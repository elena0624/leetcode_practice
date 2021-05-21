# My solution
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans=words.copy()
        for i in range(len(words)):
            biject=dict()
            used=set()
            for j in range(len(words[i])):
                if words[i][j] in biject and biject[words[i][j]] == pattern[j]:
                    continue
                elif words[i][j] not in biject and pattern[j] not in used:
                    biject[words[i][j]] = pattern[j]
                    used.add(pattern[j])
                else:
                    ans.remove(words[i])
                    break
        return(ans)
#%% Official solution1
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True

        return filter(match, words)
#%% Official solution2
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            P = {}
            for x, y in zip(pattern, word):
                if P.setdefault(x, y) != y:
                    return False
            return len(set(P.values())) == len(P.values())

        return filter(match, words)
#%% Other solution
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        b = pattern
        def is_iso(a):
            return len(a) == len(b) and len(set(a)) == len(set(b)) == len(set(zip(a, b)))
        return filter(is_iso, words)
#%% Elegant solution!!!!
def findAndReplacePattern(self, words, p):
        def F(w):
            m = {}
            return [m.setdefault(c, len(m)) for c in w]
        Fp = F(p)
        return [w for w in words if F(w) == Fp]
