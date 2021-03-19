# 70 climbing stairs
def climb(n):
    stair = [None] * 45
    stair[0]=1
    stair[1]=2
    for i in range(2,45):
        stair[i] = stair[i-2] + stair[i-1]
#    print(stair)
    print(stair[n-1])