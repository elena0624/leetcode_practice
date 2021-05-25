# My solution
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i in ["+","-","*","/"]:
                a = stack.pop()
                if i=="+":
                    stack.append(stack.pop()+a)
                elif i=="-":
                    stack.append(stack.pop()-a)
                elif i=="*":
                    stack.append(stack.pop()*a)
                elif i=="/":
                    stack.append(int(stack.pop()/a))

            else:
                stack.append(int(i))
        # return(stack.pop())
        return(stack[0])
#%% Using dictionary to call function: operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def mydiv(n1, n2):
            return int(n1/n2)
        operator_dict = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': mydiv}
        stack = []
        for c in tokens:
            if c not in operator_dict:
                stack.append(c)
            else:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                res = operator_dict[c](n1, n2)
                stack.append(str(res))
        return int(stack[-1])

#%% Using dictionary to call function: lambda
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = {
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "*": lambda x,y: x*y,
            "/": lambda x,y: x//y if x//y == x/y or x//y >= 0 else x//y+1
        }
        s = []
        for token in tokens:
            if token in operator:
                y, x = s.pop(), s.pop()
                s.append(operator[token](x, y))
            else:
                s.append(int(token))
        return s[0]