class Solution:
    def isValid(self, s: str) -> bool:
        '''This is a stack question : in python to implement stack ->
        we will use list:
        pop() for pop at end
        list[-1]for seek at top of stack 
        append()for pushing to stack '''

        '''Intuition -> for every start bracket we will push into stack
        For every corresponding closing bracket only pop from stack,
        IF at end stack is empty -> return TRUE'''

        # Optimization: A string with odd length can never have valid pairs
        if len(s) % 2 != 0:
            return False

        stack=[] #for implementing stack 

        hashmap={
            ')':'(',
            '}':'{',
            ']':'['
        } #hashmap for keeping track of which brackets are pairs

        for char in s:
            if char == '(' or char =='[' or char=='{':
                stack.append(char)
            else:
                '''if closing bracket the stack top should have 
                corresponding opening bracket'''
                top_elem=stack.pop() if stack else '#' #check is stack is empty

                if top_elem!=hashmap[char]:
                    return False
        
        return not stack #if stack not empty after execution return False else True
        