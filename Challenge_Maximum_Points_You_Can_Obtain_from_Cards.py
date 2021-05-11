class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        sum_n = sum(cardPoints)
        sum_other = sum(cardPoints[:(n-k)])
        min_other = sum_other

        for i in range(n-k,n):
            #print(i)
            sum_other = sum_other+cardPoints[i]-cardPoints[i-n+k]
            min_other = min(min_other,sum_other)

        return(sum_n-min_other)