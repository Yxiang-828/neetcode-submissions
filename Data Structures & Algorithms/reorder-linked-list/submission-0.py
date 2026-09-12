# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        front=head
        dummy=front
        if dummy==None:
            return None
        dummylists=[]
        while dummy!=None:
            dummylists.append(dummy)
            dummy=dummy.next
        back=dummylists[-1]
        ans=ListNode()
        ans.next=front
        n=len(dummylists)
        left=0
        right=n-1
        while left<=right:
            ans.next=dummylists[left]
            ans=ans.next
            ans.next=dummylists[right]
            ans=ans.next
            left+=1
            right-=1
        ans.next=None
        return