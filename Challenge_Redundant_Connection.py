class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        new_edges=collections.defaultdict(set)# 用來記錄每個點可以到哪裡

        def bfs(a):
            seen=set()
            stack=list(new_edges[a])
            while stack:
                cur=stack.pop()
        #        if cur==b:
        #            return True
                if cur in seen:
                    continue
                seen.add(cur)
                stack.extend(new_edges[cur])
                new_edges[a].add(cur)
                new_edges[cur].add(a)
        for a,b in edges:   
            # 檢查是否已經可傳入
            bfs(a)
            if a in new_edges[b] or b in new_edges[a]:
                return([a,b])
            # 沒有的話更新
            new_edges[a].add(b)
            new_edges[b].add(a)
#%%
class Solution(object):
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)
#%%
class DSU(object):
    def __init__(self):
        self.par = list(range(1001))# 紀錄x那個node的parent(那一區塊最小的)
        self.rnk = [0] * 1001
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])# 把各parent更新成該塊最小的
        return self.par[x]
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y) # 針對兩個node，去紀錄他們家最小的
        if xr == yr:# 如果已經隸屬同一個parent，代表要形成cycle了
            return False
        elif self.rnk[xr] < self.rnk[yr]:# 如果是不同的parent，那要改會影響比較少的那個
            self.par[xr] = yr # 把xr的parent改成yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr # 把yr的parent改成xr
        else:
            self.par[yr] = xr # 把yr的parent改成xr
            self.rnk[xr] += 1 # xr的權重+1
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge
#%%
class DSU:
    def __init__(self):
        self.par = list(range(1001))
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        self.par[self.find(x)] = self.find(y)
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge
#%%
class Solution:
    def findRedundantConnection(self, edges):
        parent = [0] * len(edges)

        def find(x):
            if parent[x] == 0:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            parent[rootX] = rootY
            return True

        for x, y in edges:
            if not union(x - 1, y - 1): 
                return [x, y]
#%%
from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]: 
        # union find
        parents, ranks = {}, {}
        
        def findParent(n, parents):
            while parents[n] != n:
                parents[n] = parents[parents[n]]
                n = parents[n]
            return n
        
        for edge in edges:
            u = edge[0]
            v = edge[1]
            
            if u not in parents:
                parents[u] = u
                ranks[u] = 1
            if v not in parents:
                parents[v] = v
                ranks[v] = 1
                
            pu = findParent(u, parents)
            pv = findParent(v, parents)
            
            if pu == pv:
                return edge
            
            if ranks[pu] < ranks[pv]:
                parents[pu] = pv
                ranks[pv] += ranks[pu]
            else:
                parents[pv] = pu
                ranks[pu] += ranks[pv]