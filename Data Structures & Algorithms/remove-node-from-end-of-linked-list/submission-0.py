# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''We will use fast and slow pointers here 
        we will make the fast pointer go 'n' places front of slow pointer
        at first and then update both by 1 such that when fast reaches end 
        slow is at n places from end  '''

        if not head :
            return None

        slow=head # 1x pointer
        fast=head # nx pointer
        
        for _ in range(n):
            fast=fast.next
        
        # FIX: If fast is None, it means n equals the length of the list.
        # This means we need to remove the head node.
        if not fast:
            return head.next

        temp=None # in this slow stores the before address before moving 

        while fast:
            temp=slow
            slow=slow.next
            fast=fast.next

        #when fast is at end slow is n places from end 
        if temp:
            temp.next=slow.next
        return head 





