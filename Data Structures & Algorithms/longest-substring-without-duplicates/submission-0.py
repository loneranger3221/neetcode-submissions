class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''THis is a classic variable size sliding window problem
        We can use a hashset to see which characters are present 
        to check for duplicates'''

        left=0
        hashset=set()

        result=0 #tracks final result
        longest=0 #tracks intermediate count

        '''keep iterating right pointer and update left pointer only 
        when window condition becomes invalid'''
        right=0
        
        for right in range(len(s)):
            c=s[right]
            
            '''if c already exists in hashset it means its present
            in current longest substring so we gotta remove all 
            character before it from substring'''

            while c in hashset and left<right:
                char_to_remove=s[left]
                hashset.remove(char_to_remove)
                left+=1
                longest-=1
            
            hashset.add(c)
            longest+=1

            result=max(result,longest)

        return result
        