class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import math
        majfreq=math.ceil(len(nums)/2)
        
        from collections import defaultdict
        hashmap=defaultdict(int)

        for elem in nums:
            if hashmap[elem]+1==majfreq:
                return elem
            else:
                hashmap[elem]+=1