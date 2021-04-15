# My solution
class Solution:
    def fib(self, n: int) -> int:
        dp_1=0
        dp=1
        cur=0
        if n==0:
            return(dp_1)

        for i in range(n-1):
            cur=dp_1+dp
            dp_1=dp
            dp=cur
        return(dp)

#%% Other solution => Math
def fib(self, N):
	golden_ratio = (1 + 5 ** 0.5) / 2
	return int((golden_ratio ** N + 1) / 5 ** 0.5)
#%% recursive #not recommended O(2^n)
def fib(N):
	if N == 0: return 0
	if N == 1: return 1
	return fib(N-1) + fib(N-2)
#%% hash table
memo = {}
def fib(N):

	if N == 0: return 0
	if N == 1: return 1

	if N-1 not in memo: memo[N-1] = fib(N-1)
	if N-2 not in memo: memo[N-2] = fib(N-2)

	return memo[N-1] + memo[N-2]
#%% using LRU
from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def fib(self, n: int) -> int:
        if n < 2: return n
        return self.fib(n-1) + self.fib(n-2)
#%% space optimized (only save the last2)
def fib(N):
	if N == 0: return 0
	memo = [0,1]
	for _ in range(2,N+1):
		memo = [memo[-1], memo[-1] + memo[-2]]

	return memo[-1]
#%% using tuple for above
def fib(N):
	if N == 0: return 0
	memo = (0,1)
	for _ in range(2,N+1):
		memo = (memo[-1], memo[-1] + memo[-2])

	return memo[-1]
or some math
