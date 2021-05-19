# My solution(slow- like approach1)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        memo = collections.defaultdict(int)

        def check_pre(cur_str):
            if memo[cur_str]:
                return memo[cur_str]
            remove_chr = [cur_str[:k-1]+cur_str[k:] for k in range(1,len(cur_str))]+[cur_str[:-1]]
            max_step=1
            for i in range(len(words)):
                if words[i] in remove_chr:
                    cur_step = check_pre(words[i])+1
                    max_step=max(max_step,cur_step)
            memo[cur_str]=max_step
            return max_step

        ans= 0
        for i in range(len(words)):
            check_pre(words[i])
            ans=max(memo[words[i]],ans)

        return(ans)
#%% Approach2 fast
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda x:len(x))
        memo = collections.defaultdict(int)
        ans=0
        for i in range(len(words)):
            cur_longest=1
            remove_chr = [words[i][:k-1]+words[i][k:] for k in range(1,len(words[i]))]+[words[i][:-1]]
            for j in remove_chr:
                if memo[j]:
                    cur_longest=max(cur_longest,memo[j]+1)
            memo[words[i]]=cur_longest
            ans=max(ans,cur_longest)
        return(ans)
#%% Approach2 elegant
class Solution:
    def longestStrChain(self, words):
            dp = {}
            for w in sorted(words, key=len):
                dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
            return max(dp.values())
#%% Fastest answer
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def get_predecessors(node):
            res = []
            n = len(node)
            for i in range(n):
                word = node[:i] + node[i+1:]
                if word in length_hashmap[n-1]:
                    res.append(word)
            return res
            
        def dfs(node):
            visited.add(node)
            count = 0
            for predecessor in get_predecessors(node):
                # we don't need to check visited set here, based on the problem definition
                # we will not revisit a node if we trace the words chain backward.
                if predecessor not in visited:
                    count = max(count, dfs(predecessor))
            return count + 1
            
        # build length_hashmap to save neighbor lookup time
        length_hashmap = collections.defaultdict(set)
        for word in words:
            length_hashmap[len(word)].add(word)    
        
        visited = set()
        longest = 0
        min_length = min(length_hashmap)
        # start from the longest words
        for length in sorted(length_hashmap, reverse=True):
            for word in length_hashmap[length]:
                # skipping checking captured/visited nodes 
                if word in visited:
                    continue
                longest = max(longest, dfs(word))
                # no enough words to break the record
                if length - min_length < longest:
                    return longest
        return longest