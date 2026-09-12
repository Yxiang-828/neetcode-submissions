# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        curr=head
        prev=curr
        future=curr.next
        dummylist=[]
        dummy=curr
        while dummy!=None:
           dummylist.append(dummy)
           dummy=dummy.next
        #now i have a list of dummies who point to actual node
        m=len(dummylist)
        if m==1:
            return None
        index=m-n
        if index==0:
            return head.next
        #i want prev to point to future, skip curr. curr point to None
        for i in range(index):
            prev=curr
            curr=future
            future=future.next
        #reached
        prev.next=future
        curr.next=None
        return head
        