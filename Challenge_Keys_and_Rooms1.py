# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 19:18:15 2021

@author: ppj
"""

# 3/20 keys and rooms

rooms = [[1,3],[3,0,1],[2],[0]]
room_record = []
# 先記錄第一層可以通到的地方
room_record.append(rooms[0])
print(room_record)



# 第二層可以連到的地方
room_record.append(list(set(sum(list(rooms[i] for i in room_record[0]),[]))))
print(room_record)
# 第三層可以連到的地方
room_record.append(list(set(sum(list(rooms[i] for i in room_record[1]),[]))))
print(room_record)

#%%
#rooms = [[1,3],[3,0,1],[2],[0]]
rooms = [[1],[2],[3],[]]
room_record = []
# 第一層
idx=0
room_record.append(rooms[0])
# room record=紀錄這層新增的房間
# temp_keys=目前所有可以進出的房間

# 第二層 因為可以走回去 所以先加進去
idx=1
temp_keys=[0]
temp_keys = temp_keys + room_record[idx-1]
room_record.append([])
for i in room_record[idx-1]:
    for key in rooms[i]:
        if key not in temp_keys:
            temp_keys = temp_keys + [key]
            room_record[idx].append(key)
print(room_record)
print(temp_keys)
# 第三層 針對新增的房間再去紀錄
idx=2
room_record.append([])
for i in room_record[idx-1]:
    for key in rooms[i]:
        if key not in temp_keys:
            temp_keys = temp_keys + [key]
            room_record[idx].append(key)
print(room_record)
print(temp_keys)
#%%
# 把以上寫成完成的
rooms = [[1,3],[3,0,1],[2],[0]]
# room record=紀錄這層新增的房間
# temp_keys=目前所有可以進出的房間
# 初始化第0間房新增的房間與目前所有可進去的房間
room_update = [rooms[0]]
keys = list(set([0] + rooms[0]))
# 持續探索新房間值到沒有新增的房間/或已遍歷完所有房間
idx=0
while (len(keys)<len(rooms)):# 當還有房間沒有探索完畢
    if not (room_update[idx]):# 若已經沒有可探索的房間(可探索的房間為空)
        print('False')
        break
    room_update.append([]) # 紀錄這層新增的房間
    for i in room_update[idx]: # 前一層新增的房間裡面
        for key in rooms[i]: # 的每一把鑰匙
            if key not in keys:# 若可以抵達新房間
                keys.append(key) # 則記錄這些新房間到所有可進去的
                room_update[idx+1].append(key) # 跟這層新增的
    idx = idx+1 # 繼續下一層的探索
print('True')

    


# 每次針對新的門去做就好
#for i in range(1,len(rooms)):
#    room_record.append(list(set(sum(list(rooms[i] for i in room_record[i-1]),[]))))