# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:59:14 2021

@author: ppj
"""

#A = [2,7,11,15]
#B = [1,10,4,11]

A = [12,24,8,32]
B = [13,25,32,11]

 # A_argsort = [i for (v, i) in sorted((v, i) for (i, v) in enumerate(A))]
A_sorted = sorted(A)
B_argsort = [i for (v, i) in sorted((v, i) for (i, v) in enumerate(B))]
B_sorted = sorted(B)
temp_A = A.copy()
discard_A = []


# 
index=0
index2=0
search_undone = True
# argsort一下B
for i in range(len(A)):
    B_value = B_sorted[i]
    print('i',i)
    print('index',index)
    print('B_value',B_value)
    print('A_sorted[index]',A_sorted[index])
    if search_undone:
        while (A_sorted[index]<=B_value) and (index<len(A)-1):
            discard_A.append(A_sorted[index])
            index += 1
            print('discard_A',discard_A)
        # 終於找到了或已經找到頭
        if (A_sorted[index]>B_value) and (index<len(A)-1):# 有找到比較大的且還沒到頭(要繼續找)
            temp_A[B_argsort[i]]=A_sorted[index]
            index += 1
            print('temp_A',temp_A)
        elif index==len(A)-1: # 最後一個了 不管大小就放上去
            temp_A[B_argsort[i]]=A_sorted[index]
            search_undone= False
    else: 
        temp_A[B_argsort[i]]=discard_A[index2]
        index2 += 1
        print('index2',index2)
        print('temp_A',temp_A)
print(temp_A)
    
    

    
#%%
# 空間改良1 理論上每丟一個之後就要補一個，所以可以直接補在後面
#A = [2,7,11,15]
#B = [1,10,4,11]
#
#A = [12,24,8,32]
#B = [13,25,32,11]

A = [6,3,5,2,4]
B = [9,10,7,1,8]
# ANS=[6,5,4,2,3]
 # A_argsort = [i for (v, i) in sorted((v, i) for (i, v) in enumerate(A))]
A_sorted = sorted(A)
B_argsort = [i for (v, i) in sorted((v, i) for (i, v) in enumerate(B))]
B_sorted = sorted(B)
temp_A = [None]*len(A)
#discard_A = []


# 
index=0
front_get=0 # 從前面更幾次
back_get=0 #從後面更幾次
index2=len(A)-1
#search_undone = True
# argsort一下B
for i in range(len(A)):
    B_value = B_sorted[i]
    print('i',i)
    print('index',index)
    print('index2',index2)
    print('B_value',B_value)
    print('A_sorted[index]',A_sorted[index])
#    if search_undone:
    while (A_sorted[index]<=B_value) and (index<len(A)-1):# 還沒找到且還有得找
        print('進入這裡因為A_sorted[index]<=B_value且index<index2所以要把比較小的丟補到最大的去')
        print('index',index)
        print('index2',index2)
#            discard_A.append(A_sorted[index])# 直接補在後面
        temp_A[B_argsort[index2]] = A_sorted[index] # 直接補在後面
        back_get+= 1
        print('剛剛把temp_A裡面B最大的地方就是',B_argsort[index2],'補成A_sorted[index]就是',A_sorted[index])
        print('B_argsort[index2]',B_argsort[index2])
        print('temp_A',temp_A)
        # 發現補到要丟的位置就break
        # 雖然還沒找到,但如果已經填完了
        if (front_get + back_get)==len(A):
            break
        index += 1 #去找下一個
        index2 -= 1 #後面已經補到哪一位
        print('A_sorted[index]',A_sorted[index])
#    if index==len(A-1):
#        break
    # 如果補完就結束
#    if index+index2:
#        print('進入這裡是因為index2==index剛剛看的已經補到第index2小的數=第index大的數了')
#        print('index',index)
#        print('index2',index2)
#        break
    

#    if (A_sorted[index]>B_value):
    print('這邊因為已經找到A裡面比B大的數了所以把tempA裡面B第',i,'小的位置',B_argsort[i],'存成A_sorted[',i,']')
    temp_A[B_argsort[i]]=A_sorted[index] # 跳出之後就可以存
    index += 1
    front_get +=1
    print('here index', index)
    print('here index2', index2)
    # 發現剛補完就break
#    if index2==index: #還沒check到的尾端
#        break
    print('temp_A',temp_A)
    if (front_get + back_get)==len(A):
        break
#     and (index<len(A)-1):# 有找到比較大的且還沒到頭(要繼續找)
#    elif index==len(A)-1: # 最後一個了 不管大小就放上去
#        temp_A[B_argsort[i]]=A_sorted[index]
#            search_undone= False
#    else: # 直接補在後面 就不用用了
#        temp_A[B_argsort[i]]=discard_A[index2]
#        index2 += 1
#        print('index2',index2)
#        print('temp_A',temp_A)
print(temp_A)

#%% 稍微優化
#A = [2,7,11,15]
#B = [1,10,4,11]
##
#A = [12,24,8,32]
#B = [13,25,32,11]

A = [6,3,5,2,4]
B = [9,10,7,1,8]


A_sorted = sorted(A)
B_argsort = [i for (v, i) in sorted((v, i) for (i, v) in enumerate(B))]
B_sorted = sorted(B)
temp_A = [None]*len(A)

index=0
index2=len(A)-1
#front_get=0 # 從前面更幾次 其實會等於i前進的個數
advantage_fail=0 #從後面更幾次 其實是advanrage失敗的個數

for i in range(len(A)):
    B_value = B_sorted[i]
    while (A_sorted[index]<=B_value) and (index<len(A)-1):# 還沒找到且還有得找
        temp_A[B_argsort[index2]] = A_sorted[index] # 直接補在後面
        advantage_fail+= 1
        if (i + advantage_fail)==len(A):
            break
        index += 1 #去找下一個
        index2 -= 1 #後面已經補到哪一位
    temp_A[B_argsort[i]]=A_sorted[index] # 跳出之後就可以存
    index += 1
    if (i+1 + advantage_fail)==len(A):
        break
print(temp_A)
#print('advantage',len(A)-advantage_fail) # 有可能滿了就跳出 所以這個沒有狠準