# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 23:55:10 2021

@author: ppj
"""

matrix=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# answer=[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

# 建立一個"可以下一步"的dictionary
way_dict={}
visited={}# 後面拿來記錄用
for m in range(len(matrix)):
    for n in range(len(matrix[0])):
        way_dict[m,n]=[]
        #[是否有拜訪過,是否可到pacific,是否可到atlantic]
        visited[m,n]=[False,True if m==0 or n==0 else False, True if m==(len(matrix)-1) or n==(len(matrix[0])-1) else False]
        if m-1>=0 and matrix[m-1][n]<= matrix[m][n]:# 上
            way_dict[m,n].append([m-1,n])
        if m+1<=len(matrix)-1 and matrix[m+1][n]<= matrix[m][n]:# 下
            way_dict[m,n].append([m+1,n])
        if n-1>=0 and matrix[m][n-1]<= matrix[m][n]:# 左
            way_dict[m,n].append([m,n-1])
        if n+1<=len(matrix[0])-1 and matrix[m][n+1]<= matrix[m][n]:# 右
            way_dict[m,n].append([m,n+1])
#print(way_dict)
#print(visited)
# 光建這個就要4n^2了Q
# 然後參照keys&rooms的作法
            
            
# 這些是目的地的地方
#pacific = [[0,n] for n in range(len(matrix[0]))]+[[m,0] for m in range(len(matrix))] #左上
#atlantic = [[len(matrix)-1,n] for n in range(len(matrix[0]))]+[[m,len(matrix[0])-1] for m in range(len(matrix))] #左上
#print(pacific)
#print(atlantic)

# 之後再來實測看看
#pacific_dict = [[0,n] for n in range(len(matrix[0]))]+[[m,0] for m in range(len(matrix))] #左上
#atlantic_dict = [[len(matrix)-1,n] for n in range(len(matrix[0]))]+[[m,len(matrix[0])-1] for m in range(len(matrix))] #左上
#print(pacific)
#print(atlantic)



ans_place = []

for m in range(len(matrix)):
    for n in range(len(matrix[0])):
        # 每個地方是否可抵達
        # 下一步可去的地方
        if not visited[m,n][0]:# 如果該地方還沒去過就要開始出發
            print('沒去過',m,n)
            visited[m,n][0]=True #現在要去了
            stack_togo = way_dict[m,n] # 可以去的地方
            print('stack_togo',stack_togo)
            # 記錄一下出發點已經造訪
    #        while (stack_togo):#當還有可去的地方
            stack_togo_idx=0
            while (stack_togo and (not visited[m,n][1] or not visited[m,n][2])):#當還有可去的地方且現在兩個地方有地方還沒去過 就需要繼續走
                next_visit = stack_togo.pop()# 選一個可去的地方走
#                next_visit = stack_togo[stack_togo_idx]
#                stack_togo_idx += 1
                print('next_visit',next_visit)
                for way in way_dict[tuple(next_visit)]: #該地方可以走的下一步又列出來
                    if not visited[tuple(way)][0]:# 若該地方還沒去過 #且???
                        visited[tuple(way)][0]=True # 那接下來就去了
                        stack_togo.append(way) # 並且納入接下來要探訪的地方
                    if visited[tuple(way)][1]: # 若該位置可以去pacific
                        visited[m,n][1]=True # 把這路上所有的都更新
                    if visited[tuple(way)][2]: # 若該位置可以去atlantic
                        visited[m,n][2]=True
            # 這裡走完了記錄一下是否有達到要求
            if visited[m,n][1] and visited[m,n][2]:
                ans_place.append([m,n])
        else: # 該地已經check過結果
            print('有查看過',m,n)
            if visited[m,n][1] and visited[m,n][2]:
                ans_place.append([m,n])


print(ans_place)
#        print(m,n)

#import collections
#way_dict = collections.defaultdict(dict)
#%% 修改
#matrix=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# answer=[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
#matrix=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4],[6,7,8,9,9]]
#matrix=[[1,2,2,3],[2,3,4,4],[4,5,3,1],[6,7,4,5],[5,1,2,4]]
#matrix = [[3,3,3],[3,1,3],[0,2,4]]
matrix = [[12,7,7,14,6,17,12,17,8,18,9,5],[6,8,12,5,3,6,2,14,19,6,18,13],[0,6,3,8,8,10,8,17,13,13,13,12],[5,6,8,8,15,16,19,14,7,11,2,3],[7,18,2,7,10,10,3,14,13,15,15,7],[18,6,19,4,12,3,3,2,6,6,19,6],[3,18,5,16,19,6,3,12,6,0,14,11],[9,10,17,12,10,11,11,9,0,0,12,0],[4,13,3,0,4,12,9,5,6,17,10,11],[18,3,5,0,8,19,18,4,8,19,1,3],[16,2,14,6,4,14,7,2,9,7,13,18],[0,16,19,16,16,4,15,19,7,0,3,16],[13,8,12,8,2,3,5,18,6,15,18,6],[4,10,8,1,16,0,6,0,14,10,11,8],[7,1,3,4,11,12,9,0,6,2,17,5],[1,16,6,1,0,19,11,1,5,7,8,2],[4,1,14,13,14,7,3,7,1,9,15,18],[14,11,6,14,14,14,4,0,11,17,1,9],[3,14,2,10,3,1,9,16,1,13,0,15],[8,9,13,5,5,7,10,1,4,5,0,9],[13,16,15,5,17,6,16,13,5,7,3,15],[5,1,12,19,3,13,0,0,3,10,6,13],[12,17,9,16,16,6,2,6,12,15,14,16],[7,7,0,6,4,15,1,7,17,5,2,12],[3,17,0,2,4,5,11,7,16,16,16,13],[3,7,16,11,2,16,14,9,16,17,10,3],[12,18,17,17,5,15,1,2,12,12,5,7],[11,10,10,0,11,7,17,14,5,15,2,16],[7,19,14,7,6,2,4,16,11,19,14,14],[6,17,6,6,6,15,9,12,8,13,1,7],[16,3,15,0,18,17,0,11,3,16,11,12],[15,12,4,6,19,15,17,7,3,9,2,11]]
# 有空的input???
# 若空的直接回傳空的
if not matrix:
    print( [])

# 建立一個"可以到著走"的dictionary
way_dict={}
visited={}# 後面拿來記錄用
for m in range(len(matrix)):
    for n in range(len(matrix[0])):
        way_dict[m,n]=[]
        #[是否有拜訪過,是否可到pacific,是否可到atlantic]
        visited[m,n]=[False,False,False]
        if m-1>=0 and matrix[m-1][n]>= matrix[m][n]:# 上
            way_dict[m,n].append([m-1,n])
        if m+1<=len(matrix)-1 and matrix[m+1][n]>= matrix[m][n]:# 下
            way_dict[m,n].append([m+1,n])
        if n-1>=0 and matrix[m][n-1]>= matrix[m][n]:# 左
            way_dict[m,n].append([m,n-1])
        if n+1<=len(matrix[0])-1 and matrix[m][n+1]>= matrix[m][n]:# 右
            way_dict[m,n].append([m,n+1])
#print('way_dict',way_dict)
ans_place = []

pacific = [[0,n] for n in range(len(matrix[0]))]+[[m,0] for m in range(len(matrix))] #左上
atlantic = [[len(matrix)-1,n] for n in range(len(matrix[0]))]+[[m,len(matrix[0])-1] for m in range(len(matrix))] #左上
#print('way_dict',way_dict)
# 從終點出發
for i in pacific:
    m,n=i
    # 每個地方是否可抵達
    # 下一步可去的地方
    print('m','n',m,n)
    if not visited[m,n][1]:# 如果該地方pacific還沒去過
            print('沒去過',m,n)
            visited[m,n][1]=True #現在要去了
            stack_togo = way_dict[m,n].copy() # 可以去的地方 # 不用copy()之後way_dict會一起被pop掉!!!!
            print('stack_togo',stack_togo)
            # 記錄一下出發點已經造訪
            while (stack_togo):#當還有可去的地方
                next_visit = stack_togo.pop()# 選一個可去的地方走 
                print('next_visit',next_visit)
                visited[tuple(next_visit)][1]=True # 那接下來就去了 #++
                for way in way_dict[tuple(next_visit)]: #該地方可以走的下一步又列出來
                    if not visited[tuple(way)][1]:# 若該地方還沒去過 #且???
                        visited[tuple(way)][1]=True # 那接下來就去了
                        stack_togo.append(way) # 並且納入接下來要探訪的地方
print('----')
for i in atlantic:
    m,n=i
    # 每個地方是否可抵達
    # 下一步可去的地方
    print('m','n',m,n)
    if not visited[m,n][2]:# 如果該地方pacific還沒去過
            print('沒去過',m,n)
            visited[m,n][2]=True #現在要去了
            stack_togo = way_dict[m,n].copy() # 可以去的地方# 不用copy()之後way_dict會一起被pop掉!!!!
            print('stack_togo',stack_togo)
            # 記錄一下出發點已經造訪
            while (stack_togo):#當還有可去的地方
                next_visit = stack_togo.pop()# 選一個可去的地方走
                print('next_visit',next_visit)
                visited[tuple(next_visit)][2]=True # 那接下來就去了 #++ # why原本的不用加??還是有什麼誤會??
                for way in way_dict[tuple(next_visit)]: #該地方可以走的下一步又列出來
                    if not visited[tuple(way)][2]:# 若該地方還沒去過 #且???
                        visited[tuple(way)][2]=True # 那接下來就去了
                        stack_togo.append(way) # 並且納入接下來要探訪的地方
# 都是1的表示都可以去
for m in range(len(matrix)):
    for n in range(len(matrix[0])):
        if visited[m,n][1] and visited[m,n][2]:
            ans_place.append([m,n])
print(ans_place)