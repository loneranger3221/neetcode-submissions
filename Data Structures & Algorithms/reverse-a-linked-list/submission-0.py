# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None :
            return None
        
        p1=head #pointer to head node to reverse
        p2=p1.next #pointer to the 2nd node
        if p2 is None:
            return head
        
        #otherwise we start reversing
        while p1 is not None and p2 is not None:
            t=p2.next
            p2.next=p1
            p1=p2
            p2=t

        #make the address of the first node null
        head.next=None
        head=p1 
        return head   
            
        




