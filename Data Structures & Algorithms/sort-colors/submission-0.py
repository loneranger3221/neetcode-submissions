class Solution:
    def sortColors(self, nums: List[int]) -> None:
        '''This problem is same as Dutch Flag Algo'''
        left=0 #pointing to next suitable position of 0
        right=len(nums)-1 #pointing to next suitable position of 2
        mid=0 #explorer pointer

        while mid<=right:
            if nums[mid]==0:
                #swap left and mid
                nums[mid],nums[left]=nums[left],nums[mid]
                left+=1
                mid+=1
            elif nums[mid]==2:
                #swap right and mid but dont increment mid
                nums[mid],nums[right]=nums[right],nums[mid]
                right-=1
            else:
                #mid contains 1 so skip
                mid+=1


