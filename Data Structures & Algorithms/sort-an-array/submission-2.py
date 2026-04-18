class Solution:
    def divide(self, nums: List[int], low: int, high: int):
        if low >= high:
            return
            
        mid = (low + high) // 2  # Integer division is cleaner than int()

        self.divide(nums, low, mid)
        self.divide(nums, mid + 1, high)

        self.merge(nums, low, mid, high)

    def merge(self, nums: List[int], low: int, mid: int, high: int):
        narr = []
        left = low
        right = mid + 1

        # Compare elements from both halves and append the smaller one
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:  # Included '=' to handle duplicates safely
                narr.append(nums[left])
                left += 1
            else:
                narr.append(nums[right])
                right += 1
        
        # If there are leftovers on the left side, append them
        while left <= mid:
            narr.append(nums[left])
            left += 1
            
        # If there are leftovers on the right side, append them
        while right <= high:
            narr.append(nums[right])
            right += 1
        
        # Copy the sorted temp array back into the original nums array
        for i in range(len(narr)):
            nums[low + i] = narr[i]

    def sortArray(self, nums: List[int]) -> List[int]:
        self.divide(nums, 0, len(nums) - 1)
        return nums  # Added the missing return