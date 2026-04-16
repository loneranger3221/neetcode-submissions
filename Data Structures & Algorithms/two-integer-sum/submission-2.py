from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap=defaultdict(int)
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in hashmap and hashmap[diff]!=i :
                return [hashmap[diff],i]
            else:
                hashmap[nums[i]]=i
                    