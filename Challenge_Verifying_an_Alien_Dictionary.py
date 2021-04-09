class Solution: #Set dictionary to find order position
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ords_dic = {v:k for k,v in enumerate(order)} # 不知道這跟myString.find('s')誰比較快 但後者應該不用多餘的空間 可比比看
        for i in range(len(words)-1):
            # 比較前後兩個
            s1=words[i]
            s2=words[i+1]
            s_idx=0
            while s_idx<len(s1):
                if s_idx==len(s2):# s2不能先結束 因為空集合應該在最前面
                    return(False)#
                if ords_dic[s1[s_idx]]>ords_dic[s2[s_idx]]:
                    return False
                elif ords_dic[s1[s_idx]]==ords_dic[s2[s_idx]]:
                    s_idx+=1
                else:# OK沒問題
                    break
        return(True)
#%% 
class Solution: # Use built-in str.find('x') to find position. The results are the same.
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            # 比較前後兩個
            s1=words[i]
            s2=words[i+1]
            s_idx=0
            while s_idx<len(s1):
                if s_idx==len(s2):# s2不能先結束 因為空集合應該在最前面
                    return(False)#
                if order.find(s1[s_idx])>order.find(s2[s_idx]):
                    return False
                elif order.find(s1[s_idx])==order.find(s2[s_idx]):
                    s_idx+=1
                else:# OK沒問題
                    break
        return(True)