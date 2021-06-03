class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)

        max_h=horizontalCuts[0]
        for i in range(1,len(horizontalCuts)):
            max_h=max(max_h,horizontalCuts[i]-horizontalCuts[i-1])
        max_h=max(max_h,h-horizontalCuts[-1])

        max_w=verticalCuts[0]
        for i in range(1,len(verticalCuts)):
            max_w=max(max_w,verticalCuts[i]-verticalCuts[i-1])
        max_w=max(max_w,w-verticalCuts[-1])

        mod=10**9+7

        # return((max_h%mod)*(max_w%mod))
        return((max_h*max_w)%mod)