# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''Optimal Way -> Reverse and Merge->
        1) Find the middle of the linked list
        2) Reverse the second half of the list.
        3) Merge the two halves one-by-one '''
        

        # finding middle of the linked list using Floyd Algo
        slow=head #1x
        fast=head #2x
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #at end slow pointer points to middle, using this reverse second part
        prev=None
        curr=slow.next
        slow.next=None #breaking connection btw first and second half 

        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        

        #merging the original half and reversed half one by one 
        p1=head
        p2=prev #as at last of reversing rev points to last node 
        
        while p2:  # The second half is always equal to or shorter than the first half
            temp1 = p1.next
            temp2 = p2.next
            
            # Interleave nodes
            p1.next = p2
            p2.next = temp1
            
            # Move pointers forward
            p1 = temp1
            p2 = temp2










