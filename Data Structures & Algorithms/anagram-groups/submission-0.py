from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for elem in strs:
            key=''.join(sorted(elem))
            hashmap[key].append(elem)
        return list(hashmap.values())
        