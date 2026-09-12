# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #many ways to this. 
        #slow fast pointers is one way
        #i still dont understand how does slow +1 fast +2 always meet each other as long as its not acyclic.
        if head==None:
            return False
        slow=head
        fast=head
        while slow.next != None and fast.next != None  and fast.next.next != None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True 
        return False