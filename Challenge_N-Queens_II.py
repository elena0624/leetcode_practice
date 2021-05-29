# My solution
class Solution:
    def totalNQueens(self, n: int) -> int:
        not_used=set(range(n))
        dia=set()
        andia=set()

        ans=0

        def dfs(ls,not_used,dia,andia,ans):
            if len(ls)==n:
                return ans+1
            for i in not_used:
                cur_not_used=not_used.copy()
                cur_dia=i-(len(ls)+1)
                cur_andia=i+len(ls)+1
                if (cur_dia not in dia) and (cur_andia not in andia):# 如果可安全插入
                    ls.append(i)
                    dia.add(cur_dia)
                    andia.add(cur_andia)
                    cur_not_used.remove(i)
                    ans=dfs(ls,cur_not_used,dia,andia,ans)
                    ls.pop()
                    dia.remove(cur_dia)
                    andia.remove(cur_andia)
            return ans
        return(dfs([],not_used,dia,andia,ans))
#%% Other solution
class Solution:
    def totalNQueens(self, n: int) -> int:
        count = [0]
        col = [0 for _ in range(n)]
        diag1 = [0 for _ in range(1+2*(n-1))]
        diag2 = [0 for _ in range(1+2*(n-1))]
        search(count, col, diag1, diag2, n, 0)
        return count[0]

def search(count, col, diag1, diag2, n, y):
    if y == n:
        count[0] += 1
        return
    for x in range(n):
        if col[x] or diag1[x+y] or diag2[x-y+n-1]:
            continue
        col[x], diag1[x+y], diag2[x-y+n-1] = 1, 1, 1
        search(count, col, diag1, diag2, n, y+1)
        col[x], diag1[x+y], diag2[x-y+n-1] = 0, 0, 0
#%% My other solution
class Solution:
    def totalNQueens(self, n: int) -> int:
        not_used=set(range(n))
        dia=set()
        andia=set()
        row=0
        ans=0

        def dfs(row,not_used,dia,andia,ans):
            if row==n:
                return ans+1
            for i in not_used:
                cur_not_used=not_used.copy()
                cur_dia=i-(row+1)
                cur_andia=i+row+1
                if (cur_dia not in dia) and (cur_andia not in andia):# 如果可安全插入
                    row+=1
                    dia.add(cur_dia)
                    andia.add(cur_andia)
                    cur_not_used.remove(i)
                    ans=dfs(row,cur_not_used,dia,andia,ans)
                    row-=1
                    dia.remove(cur_dia)
                    andia.remove(cur_andia)
            return ans
        return(dfs(row,not_used,dia,andia,ans))
