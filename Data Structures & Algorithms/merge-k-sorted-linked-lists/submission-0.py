# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
ListNode.__lt__=lambda self,other:self.val<other.val
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for listy in lists:
            curr=listy
            while curr!=None:
                heapq.heappush(heap,curr)
                curr=curr.next
        ans=ListNode()
        follow=ans
        while heap:
            follow.next=heapq.heappop(heap)
            follow=follow.next
        return ans.next