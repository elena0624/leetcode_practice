# My solution. Extremely slow
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes=list(dominoes)

        tmp=dominoes.copy()
        # 每一步先檢查自己的左右邊
        for i in range(len(dominoes)):
            # 會有幾種情況:
            # 如果自己本身已有方向 就不用考慮
            if dominoes[i]=='.':
                # 左非R右L>L
                if i<len(dominoes)-1 and (i==0 or dominoes[i-1]!='R') and dominoes[i+1]=='L':
                    tmp[i]='L'
                # 左R右非L>R
                elif i>0 and dominoes[i-1]=='R' and (i==len(dominoes)-1 or dominoes[i+1]!='L'):
                    tmp[i]='R'
            # 左.右.>.
            # 左R右L>.
        # 這只有考慮到隔壁步，現在要繼續考慮，直到???=>直到兩輪下來結果相等 不再變化
        while dominoes!=tmp:
            dominoes=tmp.copy()
            for i in range(len(dominoes)):
                # 會有幾種情況:
                # 如果自己本身已有方向 就不用考慮
                if dominoes[i]=='.':
                    # 左非R右L>L
                    if i<len(dominoes)-1 and (i==0 or dominoes[i-1]!='R') and dominoes[i+1]=='L':
                        tmp[i]='L'
                    # 左R右非L>R
                    elif i>0 and dominoes[i-1]=='R' and (i==len(dominoes)-1 or dominoes[i+1]!='L'):
                        tmp[i]='R'
        return(''.join(dominoes))
#%% Approach 1. O(n). find 3 patterns
class Solution(object):
    def pushDominoes(self, dominoes):
        def cmp(a, b):
            return (a > b) - (a < b) 
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i+1, j):
                    ans[k] = x
            elif x > y: #RL
                for k in range(i+1, j):
                    ans[k] = '.LR'[cmp(k-i, j-k)]

        return "".join(ans)
#%% Approach 2. O(2n). Force
class Solution(object):
    def pushDominoes(self, dominoes):
        N = len(dominoes)
        force = [0] * N

        # Populate forces going from left to right
        f = 0
        for i in range(N):
            if dominoes[i] == 'R': f = N
            elif dominoes[i] == 'L': f = 0
            else: f = max(f-1, 0)
            force[i] += f

        # Populate forces going from right to left
        f = 0
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L': f = N
            elif dominoes[i] == 'R': f = 0
            else: f = max(f-1, 0)
            force[i] -= f

        return "".join('.' if f==0 else 'R' if f > 0 else 'L'
                       for f in force)