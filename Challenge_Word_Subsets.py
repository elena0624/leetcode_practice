class Solution(object): # My solution, accepted but slow
    def wordSubsets(self, A, B):
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans
#%% solution in discussion more fast
class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        s = set(A)
        letters_required = {}
        for i in B:
            for j in i:
                count = i.count(j)
                if j not in letters_required or count > letters_required[j]:
                    letters_required[j] = count

        for i in A:
            for j in letters_required:
                if i.count(j) < letters_required[j]:
                    s.remove(i)
                    break
        return list(s)
#%% revised my solution for some part. More quickly
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ans_list = set(A)
        bb_counter = collections.Counter()
        for b in B:
            b_counter = collections.Counter(b)
            for b_key in b_counter.keys():
                if b_counter[b_key]>bb_counter[b_key]:
                    bb_counter[b_key]=b_counter[b_key]
        for a in A:
            a_counter = collections.Counter(a)
            for bb in bb_counter.keys():
                if a_counter[bb]<bb_counter[bb]:
                    ans_list.remove(a)
                    break
        return list(ans_list)