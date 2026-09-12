# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #sorted means non-descending order
        #1123457, i have 2 of these, i want to merge
        head=ListNode()
        curr=head
        while list1 !=None and list2 !=None:
            #when both are still plenty
            if(list1.val<list2.val):
                curr.next=list1
                list1=list1.next
            else:
                curr.next=list2
                list2=list2.next
            curr=curr.next
        if list1 != None:
            curr.next=list1
        else:
            curr.next=list2
        return head.next