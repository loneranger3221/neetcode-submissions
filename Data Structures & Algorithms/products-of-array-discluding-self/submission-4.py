class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        for elem in nums:
            if elem==0:
                continue
            else:
                prod*=elem
        prodlst=[]
        if 0 in nums:
            if nums.count(0)>1:
                return [0]*len(nums)
            else:
                prodlst=[prod if elem ==0 else 0
                for elem in nums]
        else:
            prodlst=[int(prod//elem) for elem in nums]
        return prodlst

       
        