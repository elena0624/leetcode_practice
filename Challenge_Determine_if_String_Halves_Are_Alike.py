class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return(not bool(sum(collections.Counter(s[:len(s)//2])[x] for x in ['A','E','I','O','U','a','e','i','o','u'])-sum(collections.Counter(s[len(s)//2:])[x] for x in ['A','E','I','O','U','a','e','i','o','u'])))