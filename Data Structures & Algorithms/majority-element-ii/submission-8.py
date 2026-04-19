class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''Extended Boyer-Moore Voting Algorithm'''
        
        # Step 1: Find the two most common candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                # If the current number doesn't match either candidate, 
                # both candidates lose 1 "health" point.
                count1 -= 1
                count2 -= 1
                
        # Step 2: Verify the candidates
        # Boyer-Moore only guarantees they are the *most frequent*, 
        # not that they strictly cross the n/3 threshold.
        result = []
        threshold = len(nums) // 3
        
        if nums.count(candidate1) > threshold:
            result.append(candidate1)
        if nums.count(candidate2) > threshold and candidate1 != candidate2:
            result.append(candidate2)
            
        return result