# My solution
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m=len(matrix)
        n=len(matrix[0])
        # 紀錄每一列現在紀到哪裡
        idx_ls = [0 for i in range(m)]
        stack=[]
        # 把每一列的第一個先加進去一個sorted的list
        for i in range(m):
            heapq.heappush(stack,(matrix[i][idx_ls[i]],i))
        while k>0:
            #print(k,stack)
            ans=heapq.heappop(stack)
            #print(ans)
            idx_ls[ans[1]]+=1
            #print(idx_ls)
            # 丟一個補一個 除非已經沒得補
            if idx_ls[ans[1]]<n:
                heapq.heappush(stack,(matrix[ans[1]][idx_ls[ans[1]]],ans[1]))
            k-=1
        return(ans[0])
#%% My solution 2
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m=len(matrix)
        n=len(matrix[0])
        if k<=(m*n//2):
            # 紀錄每一列現在紀到哪裡
            idx_ls = [0 for i in range(m)]
            stack=[]
            # 把每一列的第一個先加進去一個sorted的list
            for i in range(m):
                heapq.heappush(stack,(matrix[i][idx_ls[i]],i))
            while k>0:
                #print(k,stack)
                ans=heapq.heappop(stack)
                #print(ans)
                idx_ls[ans[1]]+=1
                #print(idx_ls)
                # 丟一個補一個 除非已經沒得補
                if idx_ls[ans[1]]<n:
                    heapq.heappush(stack,(matrix[ans[1]][idx_ls[ans[1]]],ans[1]))
                k-=1
            return(ans[0])

        else:
            idx_ls = [n-1 for i in range(m)]
            stack=[]
            # 把每一列的第一個先加進去一個sorted的list
            for i in range(m):
                heapq.heappush(stack,(-matrix[i][idx_ls[i]],i))
        #    print(stack)
            while (m*n-k+1)>0:
                #print(k,stack)
                ans=heapq.heappop(stack)
                #print(ans)
                idx_ls[ans[1]]-=1
                #print(idx_ls)
                # 丟一個補一個 除非已經沒得補
                if idx_ls[ans[1]]>=0:
                    heapq.heappush(stack,(-matrix[ans[1]][idx_ls[ans[1]]],ans[1]))
                k+=1
            return(-ans[0])
#%% Heap solution. Slower than mine 2.
class Solution(object):
    def kthSmallest(self, matrix, k):
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        ret = 0
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            if j+1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return ret

#%% Sorting solution. Fast!
class Solution(object):
    def kthSmallest(self, matrix, k):
        l = []
        for row in matrix:
            l += row
        return sorted(l)[k-1]
#%% Fastest solution!! Smart!
class Solution(object):
    def kthSmallest(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo<hi:
            mid = (lo+hi)//2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid+1
            else:
                hi = mid
        return lo
