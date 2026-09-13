# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
                return None
        def merge2lists(list1,list2):
            curr1=list1
            curr2=list2
            newlist=ListNode()
            shit=newlist
            
            while curr1 is not None and curr2 is not None:
                if curr1.val<curr2.val:
                    newlist.next=curr1
                    curr1=curr1.next
                else:
                    newlist.next=curr2
                    curr2=curr2.next
                newlist=newlist.next

            if curr1 is None:
                newlist.next=curr2
            else:
                newlist.next=curr1
            return shit.next

        n=len(lists)
        
        while len(lists)>1:
            merged=[]
            n=len(lists)
            for i in range(0,n,2):
                l1=lists[i]
                if i+1<n:
                    l2=lists[i+1]
                else:
                    merged.append(l1)
                    continue
                merged.append(merge2lists(l1,l2))
            lists=merged
        return lists[0]
