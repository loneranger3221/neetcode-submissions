# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''So we gotta Create a linked list containing the sum as 
        seperate digit nodes  as given in question 
        Let's iterate both together -> '''

        if not l1 and not l2 :
            return None
        
        elif not l1 or not l2 :
            return l1 if not l2 else l2
        
        #Now if both edge cases pass lets iterate the linked lists

        dummy=ListNode() #dummy node 
        p1=dummy
        
        carry=0 # for carrying over carry 
        while l1 and l2 :
            total=l1.val +l2.val +carry #carry from previous node 

            res=total%10 if total>9 else total
            carry=int(total//10) if total>9 else 0 #updating carry
            
            p1.next=ListNode(res,None)#updating result sum
            p1=p1.next

            l1=l1.next # Updating l1 and l2 pointers 
            l2=l2.next
        
        #Now if 2 numbers are not of equal length leftover nodes need to be covered
        while l1:
            total=l1.val+carry

            res=total%10 if total>9 else total
            carry=int(total//10) if total>9 else 0

            p1.next=ListNode(res,None)
            p1=p1.next
            l1=l1.next

        while l2:
            total=l2.val+carry

            res=total%10 if total>9 else total
            carry=int(total//10) if total>9 else 0

            p1.next=ListNode(res,None)
            p1=p1.next
            l2=l2.next
        
        #At end if carry is still not 0 append extra node 
        if carry!=0:
            p1.next=ListNode(carry,None)

        return dummy.next


            




