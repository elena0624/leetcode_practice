# Solution
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj=collections.defaultdict(set)
        for v1,v2 in connections:
            adj[v1].add(v2)
            adj[v2].add(v1)

        time=0
        low=[-1]*n
        ans=[]

        def dfs(cur_node:int, father:int, time:int, low:list, ans:list, adj)->int:
            low[cur_node]=time+1 # 初始的話就跟dfn是同步的
            for child in adj[cur_node]:
                if child==father: # 訪問過,如果是父節點就雙向不用再考慮一次
                    continue
                elif low[child]==-1:# 還未訪問過
                    low[cur_node] = min(low[cur_node],dfs(child,cur_node,time+1,low,ans,adj))#返回孩子最小的節點 更新下限

                else: #訪問過了且也不是父節點=> back edge??
                    low[cur_node] = min(low[cur_node],low[child])
            if low[cur_node]==time+1 and father!=-1:# 因為沒有父節點 自然也不用加入這一條edge(這一條edge不存在)
                ans.append([father,cur_node])        

            return low[cur_node]


        # 隨便取一點=>0
        dfs(0,-1,time,low,ans,adj)

        return(ans)
#%%
# Other Solution
class Solution:
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        graph = [[] for i in range(n)]
        depth = [-1] * n
        res = []
        for p, q in connections:
            graph[p].append(q)
            graph[q].append(p)
        def dfs(prev, cur, dep): # from, to, depth
            dep2 = depth[cur] = dep
            for nbr in graph[cur]:
                if nbr == prev: continue
                dep3 = depth[nbr] if depth[nbr] >= 0 else dfs(cur, nbr, dep+1)
                if dep3 > dep: res.append((cur, nbr))
                elif dep2 > dep3: dep2 = dep3
            depth[cur] = dep2
            return dep2
        
        dfs(0,0,0)
        return res