from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        lt = len(nums) // 3
        counts = Counter(nums)
        newlist = [] 
        
        for item, count in counts.items():
            if count > lt:
                newlist.append(item)
                
        return newlist