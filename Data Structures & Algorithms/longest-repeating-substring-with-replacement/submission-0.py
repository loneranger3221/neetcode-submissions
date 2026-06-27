class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''Since longest substring is mentioned , it is a 
        sliding window problem..
        INTUITION-> since we need to find the maximum window size ,
        where only 1 character is present in entire substring after replace
        
        For a window size = windowlen
        Maintain a hashmap with character frequencies ,
        No of non dominant characters= (windowlen- freq of max character)
        If this no is <= 'K', we can swap them with max character
        => length of longest=max(curr_longest,windowlen)

        => To find the max freq char in hashmap -> O(26) TC '''

        from collections import defaultdict

        if not s:
            return 0

        hashmap=defaultdict(int)
        left=0 #left pointer moves only for invalid condition
        longest=0 #to store result

        maximum=s[0] #to store max frequency element 
        right=0 #right pointer
        while right<len(s):
            c=s[right]
            hashmap[c]+=1
            if hashmap[c]>hashmap[maximum]:
                maximum=c
            '''Now checking if the present substring is valid'''
            windowlen=right-left+1
            non_dominant=windowlen-hashmap[maximum]
            
            '''If no of non dominant characters<=k it is valid 
            combination for longest'''
            if non_dominant<=k:
                longest=max(longest,right-left+1)
            
            else:
                '''Means invalid window so we will keep 
                updating  left until valid window is reached'''
                while non_dominant>k and left<right:
                    char_to_remove=s[left]
                    hashmap[char_to_remove]-=1
                    left+=1
                    # FIX: Recalculate metrics correctly from the current map state
                    windowlen = right - left + 1
                    maximum = max(hashmap, key=hashmap.get)
                    non_dominant = windowlen - hashmap[maximum]

            right+=1 #updating right to ensure after valid window it proceeds   
        '''At end of loop longest will have max substring length'''
        return longest

                

        








        