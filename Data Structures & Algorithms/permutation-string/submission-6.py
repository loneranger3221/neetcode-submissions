class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''Second technique to solve this problem:
        we can use hashtables to maintain character count and 
        use == operator to compare hashtables '''

        window_size=len(s1)
        if len(s2)<window_size:
            return False
        
        from collections import Counter 
        
        original_counts=Counter(s1)
        checkstr=''

        '''Now we will start with the intial window'''
        checkstr=s2[0:window_size]
        
        '''Checking if the first window is equal to s1'''
        check_counts=Counter(checkstr)
        if original_counts==check_counts:
            return True
        
        left=0 #for shifting the window from left 

        '''Now sliding the window for rest of the string'''
        for i in range(window_size, len(s2)):
            c=s2[i] #new character to add
            check_counts[s2[left]]-=1

            if check_counts[s2[left]]==0:
                del check_counts[s2[left]] #del lets us delete a elem in counter

            left+=1
            check_counts[c]+=1
            if original_counts==check_counts:
                return True
        
        return False
        







