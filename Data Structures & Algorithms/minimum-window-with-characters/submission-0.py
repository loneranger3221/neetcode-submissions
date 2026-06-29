from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''Since substring is mentioned lets use sliding window'''

        # Lets first see which characters are present in string t
        if not t or len(s) < len(t):
            return ""

        t_count = Counter(t)

        '''We gonna have to use a variable sliding window here '''
        left = 0
        hashmap = defaultdict(int) # To maintain which characters we encounter 
        
        # Track the actual best window coordinates instead of just length
        min_len = float("inf")
        best_window = ""

        # OPTIMIZATION: Track how many unique characters match the required count
        have = 0
        need = len(t_count)

        for right in range(0, len(s)):
            c = s[right]
            hashmap[c] += 1
            
            # If the current character satisfies the frequency requirement in t
            if c in t_count and hashmap[c] == t_count[c]:
                have += 1
            
            # WHILE current window is valid, try to shrink it from the left
            while have == need:
                # Update the smallest substring found so far
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    best_window = s[left : right + 1]
                
                # Pop the left character out of the window
                left_char = s[left]
                hashmap[left_char] -= 1
                
                # If removing this character breaks the valid window condition
                if left_char in t_count and hashmap[left_char] < t_count[left_char]:
                    have -= 1
                
                # Move the left pointer forward
                left += 1
                
        return best_window
