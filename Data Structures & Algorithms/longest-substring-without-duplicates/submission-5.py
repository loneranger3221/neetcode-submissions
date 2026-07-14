
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''This is a variable window problem '''
        if not s :
            return 0
        #else we start forming the window based on condition 
        left=0

        length=0 #for storing length 
        hashset=set() # to check if the character is in the string 

        for i in range(len(s)):
             # 1. If the character is a duplicate, shrink window from the left
            while s[i] in hashset:
                hashset.remove(s[left])
                left += 1
                
            # 2. Now it is safe to add the current character
            hashset.add(s[i])
            
            # 3. Update length using 'i' instead of a separate 'right' variable
            length = max(length, i - left + 1)

        return length 

