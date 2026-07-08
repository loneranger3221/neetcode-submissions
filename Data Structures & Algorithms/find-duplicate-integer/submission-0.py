class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
            ''' TC-> O(n)  SC-> O(n) '''

            #Bruteforce using a hashset 
            hashset=set()
            
            for elem in nums:
                if elem in hashset:
                    return elem 
                else:
                    hashset.add(elem)
             