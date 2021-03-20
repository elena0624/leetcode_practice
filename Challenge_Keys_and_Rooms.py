# slow solution(my)
class Solution1:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        room_update = [rooms[0]]
        keys = list(set([0] + rooms[0]))
        # 持續探索新房間值到沒有新增的房間/或已遍歷完所有房間
        idx=0
        while (len(keys)<len(rooms)):# 當還有房間沒有探索完畢
            if not (room_update[idx]):# 若已經沒有可探索的房間(可探索的房間為空)
                return False
            room_update.append([]) # 紀錄這層新增的房間
            for i in room_update[idx]: # 前一層新增的房間裡面
                for key in rooms[i]: # 的每一把鑰匙
                    if key not in keys:# 若可以抵達新房間
                        keys.append(key) # 則記錄這些新房間到所有可進去的
                        room_update[idx+1].append(key) # 跟這層新增的
            idx = idx+1 # 繼續下一層的探索
        return True
# dfs(example solution) DFS solution
class Solution(object):
    def canVisitAllRooms(self, rooms):
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        #At the beginning, we have a todo list "stack" of keys to use.
        #'seen' represents at some point we have entered this room.
        while stack:  #While we have keys...
            node = stack.pop() # get the next key 'node'
            for nei in rooms[node]: # For every key in room # 'node'...
                if not seen[nei]: # ... that hasn't been used yet
                    seen[nei] = True # mark that we've entered the room
                    stack.append(nei) # add the key to the todo list
        return all(seen) # Return true iff we've visited every room