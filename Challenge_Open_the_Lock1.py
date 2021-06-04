# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:30:41 2021

@author: ppj
"""

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

#deadends = ["8888"]
#target = "0009"

#deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
#target = "8888"

#deadends = ["0000"]
#target = "8888"

deadends = ["0201","0101","0102","1212","2002"]
target = "0000"

def bfs(stack,steps):
    if not stack:
        return False
    cur_stack=[]
    for i in stack:
        if i in dp or i in deadends:
            continue
        dp[i]=steps# 其實dp也可以不用記啦 可省點空間
        if i==target:
            return steps
        for j in range(4):
            up=i[:j]+str((int(i[j])+1)%10)+i[j+1:]
            dn=i[:j]+str((int(i[j])-1)%10)+i[j+1:]
#            if up not in deadends:
            cur_stack.append(up)
#            if dn not in deadends:
            cur_stack.append(dn)
    return bfs(cur_stack,steps+1)


dp={}
ans=bfs(['0000'],0)
print(ans if ans is not False else -1)

#%% From 0000 and target
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

#deadends = ["8888"]
#target = "0009"

#deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
#target = "8888"

#deadends = ["0000"]
#target = "8888"

#deadends = ["0201","0101","0102","1212","2002"]
#target = "0000"

def bfs(stack,targets,steps):
    if not stack:
        return False
    cur_stack=[]
    for i in stack:
        if i in deadends:
            continue
        deadends.add(i)
        if i in targets:
            return steps
        for j in range(4):
            up=i[:j]+str((int(i[j])+1)%10)+i[j+1:]
            dn=i[:j]+str((int(i[j])-1)%10)+i[j+1:]
            cur_stack.append(up)
            cur_stack.append(dn)
#        targets = bfs_target(cur_stack,targets,steps+1)# 從頭出發一步之後再從尾出發一步
    return bfs_target(cur_stack,targets,steps+1)
def bfs_target(cur_stack,targets,steps):
    if not targets:
        return False
    new_targets=set()
    for i in targets:
        if i in deadends:
            continue
        deadends.add(i)
        if i in cur_stack:
            return steps
        for j in range(4):
            up=i[:j]+str((int(i[j])+1)%10)+i[j+1:]
            dn=i[:j]+str((int(i[j])-1)%10)+i[j+1:]
            new_targets.add(up)
            new_targets.add(dn)
    return bfs(cur_stack,new_targets,steps+1)
    

deadends=set(deadends)
target=set([target])
#ans=bfs(['0000'],0)
ans=bfs(['0000'],target,0)
print(ans if ans is not False else -1)

#%% Use list for both side
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

#deadends = ["8888"]
#target = "0009"

#deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
#target = "8888"

#deadends = ["0000"]
#target = "8888"

#deadends = ["0201","0101","0102","1212","2002"]
#target = "0000"

def bfs(stack,targets,steps):
    if not stack:
        return False
    cur_stack=[]
    for i in stack:
        if i in deadends:
            continue
        deadends.add(i)
        if i in targets:
            return steps
        for j in range(4):
            up=i[:j]+str((int(i[j])+1)%10)+i[j+1:]
            dn=i[:j]+str((int(i[j])-1)%10)+i[j+1:]
            cur_stack.append(up)
            cur_stack.append(dn)
#        targets = bfs_target(cur_stack,targets,steps+1)# 從頭出發一步之後再從尾出發一步
    return bfs_target(cur_stack,targets,steps+1)
def bfs_target(cur_stack,targets,steps):
    if not targets:
        return False
    new_targets=[]
    for i in targets:
        if i in deadends:
            continue
        deadends.add(i)
        if i in cur_stack:
            return steps
        for j in range(4):
            up=i[:j]+str((int(i[j])+1)%10)+i[j+1:]
            dn=i[:j]+str((int(i[j])-1)%10)+i[j+1:]
            new_targets.append(up)
            new_targets.append(dn)
    return bfs(cur_stack,new_targets,steps+1)
    

deadends=set(deadends)
#target=set([target])
#ans=bfs(['0000'],0)
ans=bfs(['0000'],[target],0)
print(ans if ans is not False else -1)
#%% Use set for both side
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

#deadends = ["8888"]
#target = "0009"

#deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
#target = "8888"

#deadends = ["0000"]
#target = "8888"

#deadends = ["0201","0101","0102","1212","2002"]
#target = "0000"

def bfs(stack,targets,steps):
    if not stack:
        return False
    cur_stack=set()
    for i in stack:
        if i in deadends:
            continue
        deadends.add(i)
        if i in targets:
            return steps
        for j in range(4):
            up=i[:j]+str((int(i[j])+1)%10)+i[j+1:]
            dn=i[:j]+str((int(i[j])-1)%10)+i[j+1:]
            cur_stack.add(up)
            cur_stack.add(dn)
#        targets = bfs_target(cur_stack,targets,steps+1)# 從頭出發一步之後再從尾出發一步
    return bfs_target(cur_stack,targets,steps+1)
def bfs_target(cur_stack,targets,steps):
    if not targets:
        return False
    new_targets=set()
    for i in targets:
        if i in deadends:
            continue
        deadends.add(i)
        if i in cur_stack:
            return steps
        for j in range(4):
            up=i[:j]+str((int(i[j])+1)%10)+i[j+1:]
            dn=i[:j]+str((int(i[j])-1)%10)+i[j+1:]
            new_targets.add(up)
            new_targets.add(dn)
    return bfs(cur_stack,new_targets,steps+1)
    

deadends=set(deadends)
target=set([target])
#ans=bfs(['0000'],0)
ans=bfs(set(['0000']),target,0)
print(ans if ans is not False else -1)
#%% Only one function
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

#deadends = ["8888"]
#target = "0009"

#deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
#target = "8888"

#deadends = ["0000"]
#target = "8888"

#deadends = ["0201","0101","0102","1212","2002"]
#target = "0000"

def bfs(stack,targets,steps):
    if not stack:
        return False
    cur_stack=set()
    for i in stack:
        if i in targets:
            return steps
        if i in deadends:
            continue
        deadends.add(i)
        for j in range(4):
            up=i[:j]+str((int(i[j])+1)%10)+i[j+1:]
            dn=i[:j]+str((int(i[j])-1)%10)+i[j+1:]
            cur_stack.add(up)
            cur_stack.add(dn)
    return bfs(targets,cur_stack,steps+1)    

deadends=set(deadends)
ans=bfs(set(['0000']),set([target]),0)
print(ans if ans is not False else -1)

