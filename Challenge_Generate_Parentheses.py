class Solution(object):
    def generateParenthesis(self, n):
        ans=[]
        ans_str='('
        l_b=1
        r_b=0

        def gen_ans(ans_str,l_b,r_b):
            if l_b+r_b==2*n:
                ans.append(ans_str)
                return
            # +右括號
            if r_b!=l_b and l_b<=n:
                gen_ans(ans_str+')',l_b,r_b+1)
            # +左括號
            if l_b<n:
                gen_ans(ans_str+'(',l_b+1,r_b)
        gen_ans(ans_str,l_b,r_b)
        return ans
#%% Brue force(not recommended)
class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans
#%% same with my solution=backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans
#%% recursive
class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in xrange(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
#%% Other's solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        @functools.cache
        def generate(n: int) -> List[str]:
            if n == 0: return ['']
            if n == 1: return ['()']
            
            result = []
            for x in range(n):
                for l in generate(x):
                    for r in generate(n-1-x):
                        result.append("(" + l + ")" + r)
            
            return result
        
        return generate(n)