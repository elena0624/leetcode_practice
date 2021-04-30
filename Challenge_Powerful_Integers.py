class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans=set()
        a=0
        b=0
        while x**a+y**b<=bound:
            while x**a+y**b<=bound:
                ans.add(x**a+y**b)
                if y!=1:
                    b+=1
                else:
                    break
            b=0
            if x!=1:
                a+=1
            else:
                break
        return(list(ans))
#%% Official solution
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        a = bound if x == 1 else int(log(bound, x))
        b = bound if y == 1 else int(log(bound, y))
        
        powerful_integers = set([])
        
        for i in range(a + 1):
            for j in range(b + 1):
                
                value = x**i + y**j
                
                if value <= bound:
                    powerful_integers.add(value)
                    
                if y == 1:
                    break
            
            if x == 1:
                break
                
        return list(powerful_integers)
