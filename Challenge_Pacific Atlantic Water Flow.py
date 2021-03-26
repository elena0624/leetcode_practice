class Solution: # time cost and space use hugedQQ
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return( [])
        
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
        # 從終點出發
        for i in pacific:
            m,n=i
            # 每個地方是否可抵達
            # 下一步可去的地方
            if not visited[m,n][1]:# 如果該地方pacific還沒去過
                    visited[m,n][1]=True #現在要去了
                    stack_togo = way_dict[m,n].copy() # 可以去的地方 # 不用copy()之後way_dict會一起被pop掉!!!!
                    # 記錄一下出發點已經造訪
                    while (stack_togo):#當還有可去的地方
                        next_visit = stack_togo.pop()# 選一個可去的地方走 
                        visited[tuple(next_visit)][1]=True # 那接下來就去了 #++
                        for way in way_dict[tuple(next_visit)]: #該地方可以走的下一步又列出來
                            if not visited[tuple(way)][1]:# 若該地方還沒去過 #且???
                                visited[tuple(way)][1]=True # 那接下來就去了
                                stack_togo.append(way) # 並且納入接下來要探訪的地方
        for i in atlantic:
            m,n=i
            # 每個地方是否可抵達
            # 下一步可去的地方
            if not visited[m,n][2]:# 如果該地方pacific還沒去過
                    visited[m,n][2]=True #現在要去了
                    stack_togo = way_dict[m,n].copy() # 可以去的地方# 不用copy()之後way_dict會一起被pop掉!!!!
                    # 記錄一下出發點已經造訪
                    while (stack_togo):#當還有可去的地方
                        next_visit = stack_togo.pop()# 選一個可去的地方走
                        visited[tuple(next_visit)][2]=True # 那接下來就去了 #++
                        for way in way_dict[tuple(next_visit)]: #該地方可以走的下一步又列出來
                            if not visited[tuple(way)][2]:# 若該地方還沒去過 #且???
                                visited[tuple(way)][2]=True # 那接下來就去了
                                stack_togo.append(way) # 並且納入接下來要探訪的地方
        # 都是1的表示都可以去
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if visited[m,n][1] and visited[m,n][2]:
                    ans_place.append([m,n])
        return(ans_place)