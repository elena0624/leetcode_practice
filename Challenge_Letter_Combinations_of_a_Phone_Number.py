class Solution: # Not flexible solution
    def letterCombinations(self, digits: str) -> List[str]:
        dig_dict={}
        for i in range(2,7):
            dig_dict[str(i)]=list(map(chr,list(range(91+i*3,94+i*3))))
        dig_dict['7']=['p','q','r','s']
        dig_dict['8']=['t','u','v']
        dig_dict['9']=['w','x','y','z']

        if len(digits)==0:
            ans = []
        elif len(digits)==1:
            ans = dig_dict[digits[0]]
        elif len(digits)==2:
            ans = [a+b for a in dig_dict[digits[0]] for b in dig_dict[digits[1]]]
        elif len(digits)==3:
            ans = [a+b+c for a in dig_dict[digits[0]] for b in dig_dict[digits[1]] for c in dig_dict[digits[2]]]
        else:
            ans = [a+b+c+d for a in dig_dict[digits[0]] for b in dig_dict[digits[1]] for c in dig_dict[digits[2]] for d in dig_dict[digits[3]]]
        return(ans)
#%% 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '': return ([])
        l = len(digits)
        buttons = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
        ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        a = buttons[int(digits[0]) - 2]
        b = []
        for i in digits[1:]:
            t = int(i) - 2
            for j in buttons[t]:
                for k in a:
                    b.append(k + j)
            a, b = b, []
        return(a)
#%% revised Solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return ([])
        dig_dict={}
        for i in range(2,7):
            dig_dict[str(i)]=list(map(chr,list(range(91+i*3,94+i*3))))
        dig_dict['7']=['p','q','r','s']
        dig_dict['8']=['t','u','v']
        dig_dict['9']=['w','x','y','z']
        ans_ls=dig_dict[digits[0]]
        ans=[]
        for i in digits[1:]:
            ans_ls = [a+b for a in ans_ls for b in dig_dict[i]]
        return(ans_ls)