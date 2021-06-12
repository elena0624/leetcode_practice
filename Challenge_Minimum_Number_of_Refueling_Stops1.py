# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 19:32:32 2021

@author: ppj
"""
import heapq

target = 1
startFuel = 1
stations = []

target = 100
startFuel = 1
stations = [[10,100]]
#target = 100
#startFuel = 10
#stations = [[10,60],[20,30],[30,30],[60,40]]
stations.append([target,0])
ans=0
fuel_heap=[]
for i,j in stations:
#    i,j=k[0],k[1]
    while startFuel<i:# 油不夠
        if len(fuel_heap)==0:# 沒油加
            print("-1")
            break
        add_fuel=-1*heapq.heappop(fuel_heap)# 取出最大的
        ans+=1
        startFuel+=add_fuel
    heapq.heappush(fuel_heap,-j)# 不管油夠不夠
print(ans)

    