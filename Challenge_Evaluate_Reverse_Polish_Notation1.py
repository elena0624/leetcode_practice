# -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:33:35 2021

@author: ppj
"""

tokens = ["2","1","+","3","*"]
tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
stack=[]
for i in tokens:
#    cur=tokens.pop()
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
#print(stack.pop())
print(stack[0])
