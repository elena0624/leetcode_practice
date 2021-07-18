# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dum=ListNode()
        dum.next=head# 最頭
        tail=dum# 每次的尾
        cur=head
        tmp=head
        # 針對cur去做倒反再接回去
        
        # 不要動tmp
        while cur:
            #print('round start')
            #tmp=cur
            #print(tmp)
            prev=None
            for i in range(k):
                #print('ntmp',tmp)
                if not cur:
                    # 再翻回來好了
                    prev=None
                    while a:
                        x=a
                        a=a.next
                        x.next=prev
                        prev=x
                    #print('jere')
                    tail.next=x
                    return dum.next
                # 進行倒裝
                a=cur
                cur=cur.next
                a.next=prev
                prev=a
            # 產物是a
            tail.next=a
            # 輪到尾
            while tail.next:
                tail=tail.next
        return dum.next
#%% Other code
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        nextGroupHead, nodeNum = head, 0
        while nextGroupHead != None and nodeNum < k:
            nextGroupHead = nextGroupHead.next
            nodeNum += 1
        
        if nodeNum == k:
            # TODO: have completed the later part
            nextGroupHead = Solution.reverseKGroup(self, nextGroupHead, k)
            curTailNext = nextGroupHead
            for i in range(k):
                nextNode = head.next
                head.next = curTailNext
                curTailNext = head
                head = nextNode
            head = curTailNext
        return head;
#%% Elegant code
def reverseKGroup(self, head, k):
    dummy = jump = ListNode(0)
    dummy.next = l = r = head
    
    while True:
        count = 0
        while r and count < k:   # use r to locate the range
            r = r.next
            count += 1
        if count == k:  # if size k satisfied, reverse the inner linked list
            pre, cur = r, l
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur  # standard reversing
            jump.next, jump, l = pre, l, r  # connect two k-groups
        else:
            return dummy.next