class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        hashmap = dict() 
        result = 0 

        for right in range(len(s)):
            c = s[right]

            # Only move 'left' if the duplicate character is within the current window
            if c in hashmap and hashmap[c] >= left:
                left = hashmap[c] + 1
            
            hashmap[c] = right
            
            # Dynamically calculate the window size instead of tracking it manually
            result = max(result, right - left + 1)

        return result
