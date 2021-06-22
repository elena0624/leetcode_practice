# My code
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ls=[[1]]
        if numRows==1:
            return(ls)
        ls.append([1,1])
        if numRows==2:
            return(ls)
        for i in range(2,numRows):
            new_ls=[1]
            for j in range(1,i//2+1):
                # 如果i是偶數就是奇數個 到//2就翻轉
                # 如果i是奇數就是偶數個 +1//2翻轉除了中間的那個
                # 所以都是到//2+1翻轉 只是翻轉的數量不同
                new_ls.append(ls[i-1][j-1]+ls[i-1][j])
            if i%2==1:
                new_ls = new_ls+new_ls[::-1]
            else:
                new_ls = new_ls+new_ls[-2::-1]

            ls.append(new_ls)
        return(ls)
#%% Official Solution
class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle
#%% Other Solution
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        all_row, cur_row = [[1]], [1]
        for i in range(2, numRows+1):
            pre_row = [0] + cur_row + [0]
            cur_row = []
            
            for j in range(len(pre_row)-1):
                cur_row.append(pre_row[j] + pre_row[j+1])
            
            all_row.append(cur_row)
        
        return all_row