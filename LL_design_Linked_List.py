class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        return
    
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
        self.size=0
        # self.tail=None
        return
        
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        cur = self.head
        if index>self.size-1:
            return -1
        for i in range(index):
            if cur.next!=None:
                cur=cur.next
            else:
                return -1
        return cur.val
    
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next=self.head
        self.head=node
        self.size+=1
        return

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.size==0:
            self.addAtHead(val)
        else:
            cur=self.head
            for i in range(self.size-1):
                cur = cur.next
            cur.next = node
        self.size+=1
        return
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node=Node(val)
        if index>self.size:
            return
        if index==0:
            self.addAtHead(val)
            self.size+=1
        else: 
            prev = self.head
            for i in range(index-1): #先找到前一個
                prev=prev.next
            cur = prev.next # 再找到下一個
            prev.next=node
            node.next=cur
            self.size+=1
        return

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index>self.size-1:
            return
        if index==0:
            self.head=self.head.next
        else:
            prev = self.head
            for i in range(index-1): #先找到前一個
                prev=prev.next
            cur = prev.next.next # 再找到下一個
            prev.next=cur
            self.size-=1
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

#%%
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= len(self.arr):
            return -1
        return self.arr[index]

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.arr.insert(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.arr.append(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        self.arr.insert(index, val)
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= len(self.arr):
            return            
        del self.arr[index]


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)