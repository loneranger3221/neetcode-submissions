class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #using Collections.counter for easy check
        from collections import Counter
        if len(s)==len(t) and Counter(s)==Counter(t):
            return True
        else:
            return False