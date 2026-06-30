class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''Since input array is sorted we will use Binary Search'''
        
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1

        while left <= right:
            # Correctly offsets mid relative to the left boundary
            mid = (left+right)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1     # Target is to the right of mid
            else:
                right = mid - 1    # Target is to the left of mid
                
        return -1 # Returns integer instead of a string
