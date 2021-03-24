class Solution: # accepted but huge
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
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
            #print('i',i)
            #print('index',index)
            #print('B_value',B_value)
            #print('A_sorted[index]',A_sorted[index])
            if search_undone:
                while (A_sorted[index]<=B_value) and (index<len(A)-1):
                    discard_A.append(A_sorted[index])
                    index += 1
                    #print('discard_A',discard_A)
                # 終於找到了或已經找到頭
                if (A_sorted[index]>B_value) and (index<len(A)-1):# 有找到比較大的且還沒到頭(要繼續找)
                    temp_A[B_argsort[i]]=A_sorted[index]
                    index += 1
                    #print('temp_A',temp_A)
                elif index==len(A)-1: # 最後一個了 不管大小就放上去
                    temp_A[B_argsort[i]]=A_sorted[index]
                    search_undone= False
            else: 
                temp_A[B_argsort[i]]=discard_A[index2]
                index2 += 1
                #print('index2',index2)
                #print('temp_A',temp_A)
        return(temp_A)
#%% 改了壹些 感覺可以再想一下
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A_sorted = sorted(A)
        B_argsort = [i for (v, i) in sorted((v, i) for (i, v) in enumerate(B))]
        B_sorted = sorted(B)
        temp_A = [None]*len(A)

        index=0
        index2=len(A)-1
        front_get=0 # 從前面更幾次
        back_get=0 #從後面更幾次

        for i in range(len(A)):
            B_value = B_sorted[i]
            while (A_sorted[index]<=B_value) and (index<len(A)-1):# 還沒找到且還有得找
                temp_A[B_argsort[index2]] = A_sorted[index] # 直接補在後面
                back_get+= 1
                if (front_get + back_get)==len(A):
                    break
                index += 1 #去找下一個
                index2 -= 1 #後面已經補到哪一位


            temp_A[B_argsort[i]]=A_sorted[index] # 跳出之後就可以存
            index += 1
            front_get +=1
            if (front_get + back_get)==len(A):
                break
        return(temp_A)