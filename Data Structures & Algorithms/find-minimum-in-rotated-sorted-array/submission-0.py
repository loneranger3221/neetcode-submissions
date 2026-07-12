class Solution:
    def findMin(self, nums: List[int]) -> int:
        #we have to find the pivot element such that the next is the min

        left=0 #left_pointer 
        right=len(nums)-1 #right_pointer

        if nums[left]<=nums[right]:
            return nums[left] #if array is rotated n times so initial order

        while left<right:
            mid=(left+right)//2

            # If mid element is greater than the rightmost element,
            # the minimum must be in the right halves
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the minimum is at mid or to the left
            else:
                right = mid
                
        return nums[left]


                
