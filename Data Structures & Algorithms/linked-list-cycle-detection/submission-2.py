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
        
        slow = head #both pointers pointing to head 
        fast = head #slow will move 1x and fast will move 2x
        
        # This single line safely guards against all odd, even, and short lists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True # Cycle detected immediately
                
        return False # fast reached the end, so no cycle exists


        
        