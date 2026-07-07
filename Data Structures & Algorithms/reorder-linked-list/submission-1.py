# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''Basic bruteforce order is ->
        we can iterate the linked list once and keep the elements in
        order in an array  and then susbtitute the elements with
        the correct array elements '''

        arr=[]
        p1=head #pointer to head 
        count=0 #to counter how many elements are there 
        while p1 :
            arr.append(p1.val)
            count+=1
            p1=p1.next

        '''Now we will iterate the linked list and substitute the val 
        part as per pattern'''
        curr=head #current pointer 
        i=0 #pointer to array index 
        odd=1 #pointer for odd positions
        while curr :
            if i%2==0:
                curr.val=arr[i//2]
            else:
                curr.val=arr[count-odd]
                odd+=1
            i+=1
            curr=curr.next






