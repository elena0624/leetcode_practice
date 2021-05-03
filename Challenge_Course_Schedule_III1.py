# -*- coding: utf-8 -*-
"""
Created on Sun May  2 18:36:15 2021

@author: ppj
"""

courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
courses = [[1,2]]
courses = [[3,2],[4,3]]
#courses = [[100,2],[32,50]]
courses = [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]

courses = sorted(courses,key=lambda x:x[1])# 按照結束的早晚來排
print(courses)
currentTotalTime = 0
ans=0
taken=[]
#for i,j in courses:
while courses:
    print(taken)
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
print(ans)
#%% 參照官方approach3寫出的修改解=>TLE
courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
courses = [[1,2]]
#courses = [[3,2],[4,3]]
courses = [[100,2],[32,50]]
courses = [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]

courses = sorted(courses,key=lambda x:x[1])# 按照結束的早晚來排
#print(courses)
currentTotalTime = 0
ans=0

for i in range(len(courses)):
#    print(i)
    dur = courses[i][0]
    endd = courses[i][1]
#    print('cur courses',courses)
#    print('cur currentTotalTime',currentTotalTime)
    if currentTotalTime+dur<=endd:
#        print('ok',dur,endd)
        ans+=1
        currentTotalTime+=dur
    else: #如果超時 要交換(如果前面有比自己花時間的)
#        print('not ok',dur,endd)
        max_idx = i# 如果沒有比自己大的 那要踢掉的就是自己
        for m in range(i):
            if courses[m][0]>courses[max_idx][0]:
                max_idx = m
#        print(currentTotalTime,'-',courses[max_idx][0],'+',dur)
        currentTotalTime=currentTotalTime-courses[max_idx][0]+dur # 如果要踢掉的是別人那可能還有空間 如果踢掉的是自己那就不會變
        courses[max_idx][0]=-1 # 不管事自己還是換掉的別人 這堂課就是不行
#        print('結果',currentTotalTime)
print(ans)
#%% 參照官方approach4寫出的修改解=>accept但仍慢
courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
courses = [[1,2]]
#courses = [[3,2],[4,3]]
courses = [[100,2],[32,50]]
courses = [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]

courses = sorted(courses,key=lambda x:x[1])# 按照結束的早晚來排
#print(courses)
currentTotalTime = 0
ans=0

for i in range(len(courses)):
#    print(i)
    dur = courses[i][0]
    endd = courses[i][1]
#    print('cur courses',courses)
#    print('cur currentTotalTime',currentTotalTime)
    if currentTotalTime+dur<=endd:
#        print('ok',dur,endd)
        currentTotalTime+=dur
        courses[ans]=courses[i]
        ans+=1
    else: #如果超時 要交換(如果前面有比自己花時間的)
#        print('not ok',dur,endd)
        max_idx = i# 如果沒有比自己大的 那要踢掉的就是自己
        for m in range(ans):#只遍歷有上的
            if courses[m][0]>courses[max_idx][0]:
                max_idx = m
#        print(currentTotalTime,'-',courses[max_idx][0],'+',dur)
        currentTotalTime=currentTotalTime-courses[max_idx][0]+dur # 如果要踢掉的是別人那可能還有空間 如果踢掉的是自己那就不會變
        courses[max_idx]=courses[i] # 把該替換的換掉
#        print('結果',currentTotalTime)
print(ans)
#%% 參照approach 6 用heapq來做priority queue 讚讚讚!!!
import heapq
courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
courses = [[1,2]]
#courses = [[3,2],[4,3]]
courses = [[100,2],[32,50]]
#courses = [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]

courses = sorted(courses,key=lambda x:x[1])# 按照結束的早晚來排
#print(courses)
currentTotalTime = 0
ans=0
taken=[]
for i in range(len(courses)):
#    print(i)
    dur = courses[i][0]
    endd = courses[i][1]
#    print('cur courses',courses)
#    print('cur currentTotalTime',currentTotalTime)
    if currentTotalTime+dur<=endd:
#        print('ok',dur,endd)
        currentTotalTime+=dur
        heapq.heappush(taken,(-1*dur,endd))
        ans+=1
    else: #如果超時 要交換(如果前面有比自己花時間的)
        (tem1, tem2) = heapq.heappushpop(taken, (-1*dur,endd))
        currentTotalTime=currentTotalTime-(-1*tem1)+dur # 如果要踢掉的是別人那可能還有空間 如果踢掉的是自己那就不會變
print(ans)
#%% 上面的解精簡話
import heapq
courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
courses = [[1,2]]
#courses = [[3,2],[4,3]]
courses = [[100,2],[32,50]]
#courses = [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]

courses = sorted(courses,key=lambda x:x[1])# 按照結束的早晚來排
#print(courses)
currentTotalTime = 0
taken=[]
for i in range(len(courses)):
    dur = courses[i][0]
    ld = courses[i][1]
    if currentTotalTime+dur<=ld:
        currentTotalTime+=dur
        heapq.heappush(taken,(-1*dur))
    else: #如果超時 要交換(如果前面有比自己花時間的)
        max_dur = heapq.heappushpop(taken, -1*dur)
        currentTotalTime=currentTotalTime-(-1*max_dur)+dur # 如果要踢掉的是別人那可能還有空間 如果踢掉的是自己那就不會變
print(len(taken))