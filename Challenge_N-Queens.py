#%% My solution
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        ini_row = ["" for j in range(n)]
        for i in range(n):
            for j in range(n):
                ini_row[i]+="." if j!=i else "Q"
        used=set()
        def dfs(cur,used):
            tl = len(cur) if cur else 0
            if tl==n:
                return cur
            for j in range(n):
                if j not in used:
                    temp_sig=True
                    # 要加上去的話要檢查左上 右上(上不用因為只有一個)
                    for k in range(len(cur)):
                        if (j-(tl-k)>=0 and cur[k][j-(tl-k)]=='Q') or (j+(tl-k)<(n) and cur[k][j+(tl-k)]=='Q'):# 如果有衝突就不行
                            temp_sig=False
                            break
                    if temp_sig:
                        cur_new = cur.copy()
                        cur_new.append(ini_row[j])
                        used_new = used.copy()
                        used_new.add(j)
                        ans.append(dfs(cur_new,used_new))
        dfs([],used)
        return(list(filter(None, ans)))
#%% My solution2
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        ini_row = ["" for j in range(n)]
        for i in range(n):
            for j in range(n):
                ini_row[i]+="." if j!=i else "Q"
        used=set()
        def dfs(cur,used):
            tl = len(cur)
            if tl==n:
                ans.append(cur)
                return
            for j in range(n):
                if j not in used:
                    temp_sig=True
                    # 要加上去的話要檢查左上 右上(上不用因為只有一個)
                    for k in range(len(cur)):
                        if (j-(tl-k)>=0 and cur[k][j-(tl-k)]=='Q') or (j+(tl-k)<(n) and cur[k][j+(tl-k)]=='Q'):# 如果有衝突就不行
                            temp_sig=False
                            break
                    if temp_sig:
                        cur_new = cur.copy()
                        cur_new.append(ini_row[j])
                        used_new = used.copy()
                        used_new.add(j)
                        dfs(cur_new,used_new)
        dfs([],used)
        return(ans)
#%% My solution3
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        ini_row = ["" for j in range(n)]
        for i in range(n):
            for j in range(n):
                ini_row[i]+="." if j!=i else "Q"
        used=set()
        diag=set()
        andiag=set()
        def dfs(cur,used,diag,andiag):
            tl = len(cur)
            if tl==n:
                ans.append(cur)
                return
            for j in range(n):
                diag_cur = j-tl
                andiag_cur = j+tl
                if j not in used and diag_cur not in diag and andiag_cur not in andiag:
                    cur_new = cur.copy()
                    cur_new.append(ini_row[j])
                    used_new = used.copy()
                    used_new.add(j)
                    diag_new = diag.copy()
                    diag_new.add(diag_cur)
                    andiag_new = andiag.copy()
                    andiag_new.add(andiag_cur)
                    dfs(cur_new,used_new,diag_new,andiag_new)
        dfs([],used,diag,andiag)
        return(ans)
#%% Official Solution
class Solution:
    def solveNQueens(self, n):
        # Making use of a helper function to get the
        # solutions in the correct output format
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board
        
        def backtrack(row, diagonals, anti_diagonals, cols, state):
            # Base case - N queens have been placed
            if row == n:
                ans.append(create_board(state))
                return

            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                # If the queen is not placeable
                if (col in cols 
                      or curr_diagonal in diagonals 
                      or curr_anti_diagonal in anti_diagonals):
                    continue

                # "Add" the queen to the board
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                state[row][col] = "Q"

                # Move on to the next row with the updated board state
                backtrack(row + 1, diagonals, anti_diagonals, cols, state)

                # "Remove" the queen from the board since we have already
                # explored all valid paths using the above function call
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                state[row][col] = "."

        ans = []
        empty_board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return ans
#%% Quick solution
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        d1 = [False]*(2*n -1)
        d2 = [False]*(2*n -1)
        c = [False]*n
        
        res = []
        
        def solve(i, tmp):
            if i == n:
                res.append(list(tmp))
                return
            
            st = ''
            for j in range(n):
                if not c[j] and not d1[i+j] and not d2[i-j]:
                    c[j] = d1[i+j] = d2[i-j] = True
                    st = '.'*j + 'Q' + '.'*(n-j-1)
                    tmp.append(st)
                    solve(i+1, tmp)
                    c[j] = d1[i+j] = d2[i-j] = False
                    tmp.pop()
        
        solve(0, [])
        return res
#%% Other solution
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for i in range(n)]
        col = set()
        dia = set()
        adia = set()
        res = []
        def dfs(rem, i):
            if rem == 0:
                res.append([''.join(r) for r in board])
                return
            for j in range(n):
                if j in col or (i-j) in dia or (i+j) in adia:
                    continue
                board[i][j] = 'Q'
                col.add(j)
                dia.add(i-j)
                adia.add(i+j)
                dfs(rem-1, i+1)
                board[i][j] = '.'
                col.remove(j)
                dia.remove(i-j)
                adia.remove(i+j)
        dfs(n, 0)
        return res
#%% Other solution
def solveNQueens(self, n):
    def DFS(queens, xy_dif, xy_sum):
        p = len(queens)
        if p==n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
    result = []
    DFS([],[],[])
    return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
