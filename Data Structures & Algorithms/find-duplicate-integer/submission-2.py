class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''Second approach -> we have to reduce extra space
        Using Cycle Sort approach as integrs are from 1 to n '''

        i=0 #loop variable
        while i <len(nums):
            elem = nums[i] #element at current pos
            pos=elem-1 # actual index of elem = elem-1

            # If the current element is not in its correct place
            if nums[i] != nums[pos]:
                
                # Swap it to its correct position
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                # If it's already in the correct place, move to the next index
                # But if it matches another element at 'pos' and i != pos, it's a duplicate!
                if i != pos:
                    return elem
                i+=1
