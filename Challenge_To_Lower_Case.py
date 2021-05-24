class Solution:
    def toLowerCase(self, s: str) -> str:
        return(''.join(chr(ord(i)+32) if ord(i)>=65 and ord(i)<=90 else i for i in s))
#%%
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()