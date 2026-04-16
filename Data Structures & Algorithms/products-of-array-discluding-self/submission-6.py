class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''make a prefix and postfix array. for an element the value
        of product of all other elements is the product of all elem
        before that elem(prefix prod ) and the product of all elem
        after that elem (postfix prod)'''

        prefixprod=[nums[0],]
        postfixprod=[nums[-1],]
        
        for i in range(1,len(nums)):
            prefixprod.append(prefixprod[i-1]*nums[i])
            postfixprod.append(postfixprod[i-1]*nums[-i-1])
        postfixprod=postfixprod[: :-1]
        
        print(prefixprod,postfixprod)
        #creating the output array:
        prodexceptself=[postfixprod[1],]
        for i in range(1,len(nums)-1):
            prodexceptself.append(prefixprod[i-1]*postfixprod[i+1])
        prodexceptself.append(prefixprod[-2])
        return prodexceptself



       
        