# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        p1=list1 #pointer to first list
        p2=list2 #pointer to second list
        
        head=ListNode() #Dummynode for head
        p3=head #pointer to track new linked list

        while  p1 and  p2:

            if p1.val<=p2.val:
                p3.next=p1
                p1=p1.next
            else:
                p3.next=p2
                p2=p2.next
            
            p3=p3.next

        # storing leftover elements in either lists
        if p1:
            p3.next=p1 #if p1 elements remain
        else:
            p3.next=p2 #if p2 elements remain
            
        #returning head of new list
        return head.next

                

                




