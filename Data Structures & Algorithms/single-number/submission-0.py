class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''We will take the approach using xor ,
        xor of equal nos =0 and only unequal no will be left out'''

        output=0
        for i in nums:
            output=output^i

        return output