class MinStack:
    def __init__(self):
        self.min = float('inf')
        self.stack = []
        '''This approach uses encoded values to check for minimum->
        we Store the differences between current minimum and val 
        
        The trick is to record the difference between ->
        the pushed value and the current minimum.

        Whenever a new minimum is pushed, we store a negative encoded value,
        which signals that the minimum has changed.

        Later, when popping such a value, 
        we can decode it to restore the previous minimum.'''

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)#diff btw min and val=0 for first val
            self.min = val
        else:
            diff=val - self.min
            self.stack.append(diff)#store diff 
            if diff<0:#we found new minimum
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return

        pop_elem = self.stack.pop()

        if pop_elem < 0:#at this point minimum was changed 
            self.min = self.min - pop_elem # eg 3-(-4)=7

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min #this always stores minimum element


