# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head  :
            return None
        
        p1=head #pointer to head node to reverse
        p2=p1.next #pointer to the 2nd node
        if not p2:
            return head
        
        #otherwise we start reversing
        while p2 :
            t=p2.next
            p2.next=p1
            p1=p2
            p2=t

        #make the address of the first node null
        head.next=None
        head=p1 
        return head   
            
        




