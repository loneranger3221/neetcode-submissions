from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elemcount=Counter(nums)
        '''we obtained a hashmap of all the elements and their frequencies
           using Counter class '''
        # mostfreq=[tup[0] for tup in elemcount.most_common(k)]
        # most_common() returns list of tuples  OR->'''

        heap=[]
        for key,val in elemcount.items():
            heapq.heappush(heap,(-val,key))
        
        return [heapq.heappop(heap)[1] for i in range(k)]
        #using heap to return k most freq elememnts 
        

        