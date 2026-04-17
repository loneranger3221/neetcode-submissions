class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        '''Using Heap sort we get'''
        import heapq
        heapq.heapify(nums)
        outputlst=[]
        for i in range(len(nums)):
            num=heapq.heappop(nums)
            outputlst.append(num)
        
        return outputlst