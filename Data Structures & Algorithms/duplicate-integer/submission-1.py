class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for elem in nums:
            if elem in  hashset:
                return True
            else:
                hashset.add(elem)
        return False

