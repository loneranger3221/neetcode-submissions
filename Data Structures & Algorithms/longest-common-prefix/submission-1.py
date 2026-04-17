class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        prefix = strs[0]
        #most optimised without sorting also
        
        for string in strs[1:]:
            # While the current string doesn't start with our prefix...
            while not string.startswith(prefix):
                # ...chop off the last letter of our prefix
                prefix = prefix[:-1]
                
                # If we chopped it all the way down, there is no common prefix
                if not prefix:
                    return ""
                    
        return prefix