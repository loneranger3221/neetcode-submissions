class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''make a prefix and postfix array. for an element the value
        of product of all other elements is the product of all elem
        before that elem(prefix prod ) and the product of all elem
        after that elem (postfix prod)'''

        res = [1]*(len(nums))

        prefix = 1
        for i in range (len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        postfix = 1

        for j in range(len(nums)-1, -1, -1):
            res[j] = postfix * res[j]
            postfix = postfix*nums[j]
        

        return res




       
        