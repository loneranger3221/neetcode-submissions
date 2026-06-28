import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''This is a classic sliding window problem->

        LAZY DELETION:
        Create a max-heap of the first k elements.
        The top element is your maximum.
        Slide the window and always push the new element into the heap.
        The Fixed Step: Look at the top of the heap. 
        If its index is older than the left edge of your window, pop 
        The valid top element is your maximum for that window.'''
        
        output = []
        # Store elements as (-value, index) to track position
        max_heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(max_heap)
        
        # Max of the first window
        output.append(-max_heap[0][0])
        
        for right in range(k, len(nums)):
            # 1. Always push the new incoming element
            heapq.heappush(max_heap, (-nums[right], right))
            
            # 2. Clean the top of the heap (Your updated Step 4/5)
            # If the maximum element belongs to an old window, discard it.
            while max_heap[0][1] <= right - k:
                heapq.heappop(max_heap)
                
            # 3. The top is now guaranteed to be the max of the CURRENT window
            output.append(-max_heap[0][0])
            
        return output
