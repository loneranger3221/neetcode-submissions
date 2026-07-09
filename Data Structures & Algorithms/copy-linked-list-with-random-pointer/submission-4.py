# Definition for a Node.
'''class Node:
        def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
            self.val = int(x)
            self.next = next
            self.random = random  '''

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head :
            return None

        '''We have to create a replica of the original Linked List'''
         # Map to store {old_node: new_node}
        old_to_new = {}
        
        # Step 1: Create all new nodes with values
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        # Step 2: Connect next and random pointers
        curr = head
        while curr:
            new_node = old_to_new[curr]
            # Map next pointer using the dictionary
            new_node.next = old_to_new.get(curr.next)
            # Map random pointer using the dictionary
            new_node.random = old_to_new.get(curr.random)
            curr = curr.next
            
        return old_to_new[head]
            






        

            






        