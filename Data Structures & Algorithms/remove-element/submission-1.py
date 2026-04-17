class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val not in nums or not nums :
            return len(nums)#as val not in there all are allowed

        lstptr=len(nums)-1 # pointing to last index to swap elements from there
        i=0 # makes safe zone excluding val

        # Use <= so we don't miss evaluating the middle element when pointers meet
        while i <= lstptr:
            if nums[i] == val:
                # Swap the bad element with the last element
                nums[i], nums[lstptr] = nums[lstptr], nums[i]
                
                # Shrink the array from the right
                lstptr -= 1
                
                # CRITICAL: We do NOT increment 'i' here. 
                # We need to re-check nums[i] on the next loop because the 
                # element we just swapped in from the back might also be 'val'!
            else:
                # The element is safe, move our reader forward
                i += 1
                
        # When the loop finishes, 'i' has counted exactly how many safe elements exist
        return i
        