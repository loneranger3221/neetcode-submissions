# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''Here we will use Floyd Cycle detection method 
        using Fast and Slow pointers  is they intersect at a point
        cycle is present '''
        if not head or not head.next:
            return False
        
        flag=0 #flag variable for checking if cycle

        p1=head #first pointer goes 1x
        p2=head.next #second pointer goes 2x
        
        while p1 and p2 :
            if p1==p2:
                flag=1
                break
            else:
                if not p2.next or not p2.next.next :
                    break
                p1=p1.next
                p2=p2.next.next
        
        if flag==1:
            return True
        else:
            return False
            






        
        