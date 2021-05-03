class Solution: # My slow solution
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses,key=lambda x:x[1])# 按照結束的早晚來排
        currentTotalTime = 0
        ans=0
        taken=[]
        while courses:
            (i,j) = courses.pop(0)
            if currentTotalTime+i<=j:
                ans+=1
                currentTotalTime+=i
                taken.append([i,j])
            else: #如果超時 要交換(如果前面有比自己花時間的)
                if not taken:#如果第一個就直接放不下去就跳過讓下一個來
                    continue
                else:
                    taken = sorted(taken,key=lambda x:x[0])# 按照大小排
                    if taken[-1][0]>i:
                        out=taken.pop()# 把最大的拿走
                        # 把現在這個加進去
                        currentTotalTime=currentTotalTime-out[0]+i
                        taken.append([i,j])
        return(ans)        
#%% Revised solution based on approach 3 but TLE!
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses,key=lambda x:x[1])# 按照結束的早晚來排
        currentTotalTime = 0
        ans=0

        for i in range(len(courses)):
            dur = courses[i][0]
            endd = courses[i][1]
            if currentTotalTime+dur<=endd:
                ans+=1
                currentTotalTime+=dur
            else: #如果超時 要交換(如果前面有比自己花時間的)
                max_idx = i# 如果沒有比自己大的 那要踢掉的就是自己
                for m in range(i):
                    if courses[m][0]>courses[max_idx][0]:
                        max_idx = m
                currentTotalTime=currentTotalTime-courses[max_idx][0]+dur # 如果要踢掉的是別人那可能還有空間 如果踢掉的是自己那就不會變
                courses[max_idx][0]=-1 # 不管事自己還是換掉的別人 這堂課就是不行
        return(ans)
#%% Revised solution based on approach 4 but slower than my original solution
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses,key=lambda x:x[1])# 按照結束的早晚來排
        currentTotalTime = 0
        ans=0

        for i in range(len(courses)):
            dur = courses[i][0]
            endd = courses[i][1]
            if currentTotalTime+dur<=endd:
                currentTotalTime+=dur
                courses[ans]=courses[i]
                ans+=1
            else: #如果超時 要交換(如果前面有比自己花時間的)
                max_idx = i# 如果沒有比自己大的 那要踢掉的就是自己
                for m in range(ans):#只遍歷有上的
                    if courses[m][0]>courses[max_idx][0]:
                        max_idx = m
                currentTotalTime=currentTotalTime-courses[max_idx][0]+dur # 如果要踢掉的是別人那可能還有空間 如果踢掉的是自己那就不會變
                courses[max_idx]=courses[i] # 把該替換的換掉
        return(ans)
#%% Solution reference of approach 6 using heapq to build priority queue. Fast! Recommend!
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses,key=lambda x:x[1])# 按照結束的早晚來排
        currentTotalTime = 0
        ans=0# 可以不用, 可直接回傳len(taken就好)
        taken=[]
        for i in range(len(courses)):
            dur = courses[i][0]
            endd = courses[i][1]
            if currentTotalTime+dur<=endd:
                currentTotalTime+=dur
                heapq.heappush(taken,(-1*dur,endd))
                ans+=1 # 可以不用, 可直接回傳len(taken就好)
            else: #如果超時 要交換(如果前面有比自己花時間的)
                (tem1, tem2) = heapq.heappushpop(taken, (-1*dur,endd))
                currentTotalTime=currentTotalTime-(-1*tem1)+dur
        return(ans)
#%% Slightly modified. Optimal.
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses,key=lambda x:x[1])
        currentTotalTime = 0
        taken=[]
        for i in range(len(courses)):
            dur = courses[i][0]
            ld = courses[i][1]
            if currentTotalTime+dur<=ld:
                currentTotalTime+=dur
                heapq.heappush(taken,(-1*dur))
            else:
                max_dur = heapq.heappushpop(taken, -1*dur)
                currentTotalTime=currentTotalTime-(-1*max_dur)+dur
        return(len(taken))