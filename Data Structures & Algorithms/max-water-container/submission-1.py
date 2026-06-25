class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        p1,p2=0,len(heights)-1
        
        '''This is optimal soln using greedy strategy with just 
        slight modifications from the previous solution  '''
        
        while p1<p2:
            #area calc and updation 
            curr_max= min(heights[p1],heights[p2])*abs(p2-p1)
            if curr_max>max:
                max=curr_max

            # Move the pointer that points to the shorter line only 
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return max

