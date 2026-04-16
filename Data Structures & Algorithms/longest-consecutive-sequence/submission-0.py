import heapq
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  # for absolutely empty list 
            
        #ideaaaaaa : maybe we can use min heap 
        testlst=nums
        heapq.heapify(testlst)
        #heapify to create min heap of elements
        print(testlst)

        lscount=1
        maximum=1
        st=heapq.heappop(testlst)
        while testlst:#while loop as after each pop len is decreasing
            num=heapq.heappop(testlst)
            if num==st:
                continue
            elif abs(num-st) ==1:
                lscount+=1    
            else:
                maximum=max(maximum,lscount)
                lscount=1
            st=num
        return max(maximum,lscount)

