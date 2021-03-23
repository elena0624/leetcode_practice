class Solution1:# Wrong answer! Should check if there are Capitalization case first
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        ans_list = ['']*len(queries)
        upper_wordlist = [x.upper() for x in wordlist] # 都改成大寫
        vowel_wordlist = [x.replace('A','1').replace('E','1').replace('I','1').replace('O','1').replace('U','1') for x in upper_wordlist]# 都replace成特殊字樣
        for i in range(len(queries)):
            if queries[i] in wordlist:
                ans_list[i] = queries[i]
                continue
            upper_qword = queries[i].upper() # 開始檢查大小寫
            vowel_qword = upper_qword.replace('A','1').replace('E','1').replace('I','1').replace('O','1').replace('U','1')
            for j in range(len(wordlist)):
                if upper_qword == upper_wordlist[j]:# 若大小寫一樣
                    ans_list[i] = wordlist[j]
                    break
                elif vowel_qword == vowel_wordlist[j]:
                    # Wrong here cause if there are capitalization and vowel cases at the same time, may return the word in the front with two cases rather than the latter with only capitalzation case
                    ans_list[i] = wordlist[j]
                    break
        return ans_list

#%%
class Solution2: # Answer accepted but the runtime is extremely high
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        ans_list = ['']*len(queries)
        upper_wordlist = [x.upper() for x in wordlist] # 都改成大寫
        #print(upper_wordlist)
        vowel_wordlist = [x.replace('A','1').replace('E','1').replace('I','1').replace('O','1').replace('U','1') for x in upper_wordlist]# 都replace成特殊字樣
        #print(vowel_wordlist)
        for i in range(len(queries)):
            if queries[i] in wordlist:
                ans_list[i] = queries[i]
                continue
            upper_qword = queries[i].upper() # 開始檢查大小寫
            if upper_qword in upper_wordlist:
                ans_list[i] = wordlist[upper_wordlist.index(upper_qword)]
                continue
            vowel_qword = upper_qword.replace('A','1').replace('E','1').replace('I','1').replace('O','1').replace('U','1') # 檢查母音
            if vowel_qword in vowel_wordlist:
                ans_list[i] = wordlist[vowel_wordlist.index(vowel_qword)]
                continue
        return(ans_list)
#%% from leetcode solution
class Solution(object):
    def spellchecker(self, wordlist, queries):
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c
                           for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""

        return map(solve, queries)