class MinStack:

    def __init__(self):
        self.stack=[]# for implementing stack 

        '''self.minimum=float('inf')
        self.secmin=float('inf') this approach is only applicable for 2 pops'''

        self.minimum=[]# another stack for maintaining the minimum at each step

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_push=val if not self.minimum else min(self.minimum[-1],val)
        self.minimum.append(min_push)#this is the calc minimum for this step

    def pop(self) -> None:
        #pop from both stacks together to maintain the steps
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        #we will use the above functions to get min element in stack in O(1)
        return self.minimum[-1] #from minimum stack

        
