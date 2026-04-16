from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=defaultdict(int)
        for elem in nums:
            hashmap[elem]+=1
        sorted_list =sorted(hashmap.items(),key=lambda item:item[1],reverse=True)
        return [tup[0] for tup in sorted_list[:k]]