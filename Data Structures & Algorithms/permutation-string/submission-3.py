class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''We can solve this using sliding window 
        every permutation is of equal length as s1 ,
        and will be present as a substring in s2 so its a 
        fixed window problem '''

        window_size=len(s1)
        
        if len(s2)<window_size:
            return False
        '''Lets go with the basic assumption that for any permutation 
        if we sort the string it will give us the same result '''

        left=0
        checkstr=''
        original=''.join(sorted(s1))

        '''Creating the intital window string'''
        for i in range(0,window_size):
            checkstr+=s2[i]
        
        if ''.join(sorted(checkstr))==original:
            return True

        '''Now keep updating the fixed size window'''
        for right in range(window_size,len(s2))  :

            '''changing the window elements'''
            checkstr=checkstr[1:]+s2[right]

            windowstr= ''.join(sorted(checkstr))
            if windowstr==original:
                return True
            
        
        return False #if permutation not found after entire iteration

        






