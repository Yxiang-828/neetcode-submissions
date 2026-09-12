# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #0->1->2->3
        #0<-1<-2<-3
        # node contains value next
        # you cant read write update a node that doesnt exist
        # you want the nodes to point in the other direction
        # to point in the other direction, you cant lost track of the future because if future change direction you cant move on to the one ahead, hence you need a pointer to prempt before change
        # a<b<c -- you need a<b'<c before a<b'>c such that you can still modify it to a'>b>c
        # so say i have 
        curr=head # where head is head>whatever behind
        if not curr:
            return None
        #head needs to point to null and i still need a pointer at head and another at head->next(if exist), so that head->next can point to head
        future=curr.next
        if not future:
            return head
        curr.next=None
        #stopping condition: future =null
        while future != None:
            dummy=curr
            curr=future
            future=future.next
            curr.next=dummy
        return curr
