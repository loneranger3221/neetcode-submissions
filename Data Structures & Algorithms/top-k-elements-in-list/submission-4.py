from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''Using Bucket Sort -> O(n) Best'''
        bucketlist=[[] for i in range(len(nums)+1)]
        #creating hashmap tp keep count
        hashmap=Counter(nums)
        
        #making the bucket array
        for key,val in hashmap.items():
            bucketlist[val].append(key)
        #now extracting top k elements
        output=[]
        for i in reversed(range(len(bucketlist))):
            if len(output)==k:
                return output
            elif len(output)<k and len(output)+len(bucketlist[i])>k:
                return output.extend(bucketlist[i][:k-len(output)])
            else:
                output.extend(bucketlist[i])


