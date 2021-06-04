# My naive BFS solution. slow
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
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
                    cur_stack.append(up)
                    cur_stack.append(dn)
            return bfs(cur_stack,steps+1)

        dp={}
        ans=bfs(['0000'],0)
        return(ans if ans is not False else -1)
#%% Search from both side
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
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
        ans=bfs(['0000'],target,0)
        return(ans if ans is not False else -1)
#%% Use list
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
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
        ans=bfs(['0000'],[target],0)
        return(ans if ans is not False else -1)
#%% Use set
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
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
        #target=set([target])
        ans=bfs(set(['0000']),set([target]),0)
        return(ans if ans is not False else -1)
#%% Revised for repeated code
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
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
        return(ans if ans is not False else -1)
#%% Fastest answer
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #如果不考慮deadends 就是看順時鐘快 還是逆時鐘快
        #0~4 順 => n次
        #5 一樣 => 5次
        #6-9 逆 => 10-n次
        #遇到deadend的話就是改另個方向時針 or 先轉掉某個數字(來回一步+2)
        def int_to_str(n):# 補成4位數的string 
            n = str(abs(n))
            zero = (4-len(n)) * '0'
            return zero+n       
        
        
        def next_n(current_lock):
            def dead_test(add_n):
                nonlocal update_lock
                idx = -(len(str(abs(add_n))))
                # print(10 ** abs(idx+1),update_lock[idx])
                lock = 10 ** abs(idx+1) * int(update_lock[idx])
                # print('before',update_lock)
                temp = lock + add_n
                temp = int_to_str(temp)
                # print('now',update_lock,'add2',add_n,'=',temp,'idx',idx)
                
                
                test_lock = update_lock[:]
                test_lock[idx] = temp[idx]
                # print('test_lock',test_lock)
                if ''.join(test_lock) in deadends:
                    return False
                update_lock = test_lock
                self.count += 1
                # print('update cl',update_lock)
                return True
            
            def add_num(idx):
                nonlocal update_lock
                n = update_lock[idx]
                t = 10 ** abs(idx+1) if n > '5' else -(10 ** abs(idx+1))
                if n == '0':
                    if update_lock == current_lock:
                        hold.append(t) #暫存其他可以動的選擇 
                        hold.append(-t)
                    return 

                ok = dead_test(t)
                if not ok:
                    if update_lock == current_lock:
                        good_move.append(t)
                        hold.append(-t)
                return 
            
            def clean_good_moves():
                nonlocal good_move
                while good_move:
                    pass_ = 0
                    for n in good_move:
                        ok = dead_test(n)
                        if ok:
                            pass_ += 1
                            good_move.remove(n)
                    if pass_ == 0:
                        break
                return
            
            #----------------function code start
            #count = 0
            update_lock = current_lock[:]
            good_move = []
            hold = []
            for i in range(-4,0):                
                add_n = add_num(i) 
            
            if update_lock != current_lock:
                clean_good_moves()
                return update_lock
            
            # print('not found good match, look for optional matches.')
            if not hold:
                return False
            
            while hold:
                add_n = hold.pop()
                ok = dead_test(add_n)
                if not ok:
                    continue  
                    
                clean_good_moves()
                
                if update_lock == current_lock:
                    return False
                return update_lock
            
        
        #---------------start from target                
        self.count = 0
        target = list(target)
        if '0000' in deadends:
            return -1
        
        while target != ['0']*4:
            target = next_n(target)
            if not target:
                return -1
        
        return self.count
#%% Iteratively solution
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0
        front, back = set(['0000']), set([target])
        level = 1
        
        while front:
            new_front = set()
            for item in front:
                for i in range(len(item)):
                    for j in [(int(item[i]) + 1) % 10, (10 + int(item[i]) - 1) % 10]:
                        new_item = item[:i] + str(j) + item[i + 1:]
                        if new_item in back:
                            return level
                        if new_item in deadends:
                            continue
                        new_front.add(new_item)
                        deadends.add(new_item)
            if len(new_front) > len(back):
                new_front, back = back, new_front
            front = new_front
            level += 1
        
        return -1