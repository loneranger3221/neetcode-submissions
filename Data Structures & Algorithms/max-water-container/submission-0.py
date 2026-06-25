class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        p1,p2=0,len(heights)-1

        while p1<p2:
            curr_max= min(heights[p1],heights[p2])*abs(p2-p1)
            if curr_max>max:
                max=curr_max
            if p1==p2-1:
                p1=0
                p2-=1
            p1+=1
        return max