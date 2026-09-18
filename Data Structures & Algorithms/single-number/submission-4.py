class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''We will use Xor Operation for this O(n) TC and O(1) SC '''
        if len(nums)==1:
            return nums[0]

        output=0 # to store the output 
        for elem in nums:
            output=output^elem
        return output