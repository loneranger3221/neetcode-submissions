class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''This is a classic sliding window problem

        Intuition-> We will use a Fixed size sliding window of size k
        , and traverse it normally and maintain a max elem for list
        size of list=len(nums)-k(windowsize)+1 , also the no of times 
        window is scanned'''

        output=[] #output list
        # based on constraints nums[i] can be -ve as well
        
        maximum=nums[0]
        '''Calculating max for first window '''
        for i in range(0,k):
            if nums[i]>maximum:
                maximum=nums[i]
        '''Now that we found max for first window we can use it 
        to efficiently find max of other windows'''

        output.append(maximum)

        for right in range(k,len(nums)):
            elem_to_remove=nums[right-k]

            if elem_to_remove != maximum:
                '''We then only have to compare max to new element'''
                maximum=max(maximum,nums[right])
            else:
                '''We will now have to recalculate the maximum for the window'''
                maximum=max(nums[right-k+1:right+1])
            
            output.append(maximum)
        
        return output


        

