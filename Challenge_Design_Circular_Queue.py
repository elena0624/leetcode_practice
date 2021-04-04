class MyCircularQueue:

    def __init__(self, k: int):
        #Initializes the object with the size of the queue to be k
        self.node_ls = [None]*k            
        self.size=k
        self.nodes=0
        return
    
    def enQueue(self, value: int) -> bool:
        #Inserts an element into the circular queue. Return true if the operation is successful.
        if self.nodes == self.size:
            return False
        else:
            self.node_ls[self.nodes]=value
            self.nodes+=1
            return True
            
    
    def deQueue(self) -> bool:
        #Deletes an element from the circular queue. Return true if the operation is successful.
        if self.nodes==0:
            return False
        else:
            self.node_ls[0]=None
            for i in range(self.nodes-1):
                self.node_ls[i] = self.node_ls[i+1]
            self.nodes-=1
            return True

    def Front(self) -> int:
        # Gets the front item from the queue. If the queue is empty, return -1.
        if self.nodes==0:
            return -1
        else:
            return self.node_ls[0]

    def Rear(self) -> int:
        # Gets the last item from the queue. If the queue is empty, return -1.
        if self.nodes==0:
            return -1
        else:
            return self.node_ls[self.nodes-1]

    def isEmpty(self) -> bool:
        #  Checks whether the circular queue is empty or not.
        if self.nodes==0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        # Checks whether the circular queue is full or not.
        if self.nodes==self.size:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

#%% Better solution
class MyCircularQueue:
    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.queue = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = value
            self.size += 1
            return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front = (self.front+1) % self.max_size
            self.size -= 1
            return True
        

    def Front(self) -> int:
        return self.queue[self.front] if self.size else -1
        

    def Rear(self) -> int:
        return self.queue[self.rear] if self.size else -1
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.max_size