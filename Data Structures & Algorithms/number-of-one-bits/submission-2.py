class Solution:
    def hammingWeight(self, n: int) -> int:
        '''To find the no of set bits in the binary rep of a number 
        we will use the Brian Kernighan’s Algorithm '''
        
        num=n
        count=0
        while num:
            num=num & (num-1)
            count+=1
        return count 

        