# My bf answer. slow
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        ans=[]
        for i in range(1,len(searchWord)+1):
            ans_tp=[]
            for product in products:
                if product[:i]==searchWord[:i]:
                    ans_tp.append(product)
            ans.append(ans_tp[:3])
        return ans
#%% binary search 10X faster
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        ans=[]

        for i in range(1,len(searchWord)+1):
            j=bisect.bisect_left(products,searchWord[:i])
            print('j',j)
            ans.append([products[k] for k in range(j,j+3) if k<len(products) and products[k][:i]==searchWord[:i]])
        return(ans)    
#%% Naive binary search
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        ans=[]

        def bisect(sw):
            l=0
            r=len(products)-1
            m=(l+r)//2
            while l<r:
                m=(l+r)//2
                if sw>products[m]:# 如果位在右邊
                    l=m+1
                else: #位在左邊或上面
                    r=m
            return r
        for i in range(1,len(searchWord)+1):
            j=bisect(searchWord[:i])
            ans.append([products[k] for k in range(j,j+3) if k<len(products) and products[k][:i]==searchWord[:i]])
        return(ans)
#%% More elegant
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        curWord = ''
        products.sort()
        for cha in searchWord:
            curWord += cha
            idx = bisect.bisect_left(products, curWord)
            ans.append([product for product in products[idx:idx+3] if product.startswith(curWord)])
        return ans
#%% Using bisect right. Very Fast
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        prefix = ''
        for ch in searchWord:
            prefix += ch
            l = bisect.bisect_left(products, prefix)
            r = bisect.bisect_right(products, prefix + '~')
            if l == r: # no such word
                break 
            ans.append(products[ l : min(l+3, r) ])
        while len(ans) < len(searchWord): # append empty list when not found
            ans.append([])
        return ans
#%% Trie My Solution
class TrieNode:
    def __init__(self):
        self.isWord=False
        self.child={}

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        cur=root=TrieNode()
        for i in products:
            cur=root
            for j in i:
                if j not in cur.child:
                    cur.child[j]=TrieNode()
                cur=cur.child[j]
            cur.isWord=True
        #        print(j,ord(j)-97)


        def findprefix(s,cur):
            for i in s:
                if i in cur.child:
                    cur=cur.child[i]
                else:
                    return False  
            return cur
        def preordersearch(s, pre_cur, ans):
            if len(ans)==3:
                return ans
            if pre_cur.isWord:
                ans.append(s)
            for i in sorted(pre_cur.child):
                preordersearch(s+i,pre_cur.child[i],ans)
            return ans

        ans=[]
        cur=root
        for i in range(1,len(searchWord)+1):# 針對每鑑入
            cur_n=findprefix(searchWord[:i],cur)
            if cur_n:
                ans.append(preordersearch(searchWord[:i],cur_n,[]))
            else:
                ans.append([])
        return(ans)
#%% Trie others Solution
class Trie:
    def __init__(self):
        self.sub = {}
        self.suggestion = []
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        for product in sorted(products):
            self._insert(product, root)
        return self._search(searchWord, root)    
    def _insert(self, product: str, root: Trie) -> None:
        trie = root
        for char in product:
            if char not in trie.sub:
                trie.sub[char] = Trie()
            trie = trie.sub[char]
            trie.suggestion.append(product)
            trie.suggestion.sort()
            if len(trie.suggestion) > 3:
                trie.suggestion.pop()
    def _search(self, searchWord: str, root: Trie) -> List[List[str]]:              
        ans = []
        for char in searchWord:
            if root:
                root = root.sub.get(char)
            ans.append(root.suggestion if root else [])            
        return ans
#%% Two pointers
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(products)
        products.sort()  # Sort by increasing lexicographically order of products
        ans = []
        startIndex, endIndex = 0, n - 1
        for i, c in enumerate(searchWord):
            while startIndex <= endIndex and (i >= len(products[startIndex]) or products[startIndex][i] < c):
                startIndex += 1
            while startIndex <= endIndex and (i >= len(products[endIndex]) or products[endIndex][i] > c):
                endIndex -= 1

            suggestProducts = []
            for j in range(startIndex, min(startIndex+3, endIndex+1)):
                suggestProducts.append(products[j])
            ans.append(suggestProducts)
        return ans
