class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''BOYER MOORES ALGO'''
        candidate = None
        count = 0
        ''' TC->O(N) SC->O(1) '''
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate