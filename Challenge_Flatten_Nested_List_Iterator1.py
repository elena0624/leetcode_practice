# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 12:16:49 2021

@author: ppj
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList=nestedList
        #self.NestedInteger=NestedInteger(nestedList)
        #print(nestedList.isInteger)
        #print(nestedList.getList)
        
    
    def next(self) -> int:
        #return self.nestedList.pop().getInteger()
        print('get!!')
        return self.nestedList.pop(0).getInteger()
    
    def hasNext(self) -> bool:
        print('has next')
        print(self.nestedList)
        if not self.nestedList:
            return False
        while self.nestedList:
            pop_item = self.nestedList.pop(0)
            print('pop',pop_item)
            if pop_item.isInteger():
                print('a',pop_item.getInteger)
                self.nestedList=[pop_item]+self.nestedList
                return True    
            elif pop_item.getList():
                print('b',pop_item.getList())
                while pop_item.getList():
                    pop_item2=pop_item.getList().pop()
                    if pop_item2.isInteger or pop_item2.getList():
                        print('append')
                        self.nestedList=[pop_item2]+self.nestedList
                    # self.nestedList.append([pop_item.getList().pop()])
                    print('aa',self.nestedList)
                    print('bb',pop_item.getList())
                # pop_item = self.nestedList.pop()
                if self.nestedList[0].isInteger():
                    return True
            #else:
                #print('???')
                #return False
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())