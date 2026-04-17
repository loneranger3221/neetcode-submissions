class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        # Sort alphabetically (lexicographically)
        strs.sort() 
        
        first = strs[0]
        last = strs[-1]
        ans = ""
        
        # We only need to compare the first and last strings!
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            ans += first[i]
            #TC-O(NlogN)
        return ans