class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''We can also use a hashset to check which appears once '''
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return list(seen)[0]