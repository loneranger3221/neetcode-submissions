class Solution:
    def trap(self, height: List[int]) -> int:

        leftmax=[0]*len(height)
        rightmax=[0]*len(height)

        for i in range(1,len(height)):
            leftmax[i]=max(leftmax[i-1],height[i-1])
        
        for i in range(len(height)-2 ,0,-1):
            rightmax[i]=max(rightmax[i+1],height[i+1])

        '''left max and right max array for each position is created
        now we can directly apply formula at each index to calculate
        total trapped water'''
        
        trapped_water=0
        for i in range(0,len(height)):
            water_allowed=min(leftmax[i],rightmax[i])-height[i]
            trapped_water+=water_allowed if water_allowed>0 else 0
        
        '''Now we can return the trapped_water amount'''
        return trapped_water


        '''Approach 1 : water trapped at each pos i =>

            min(left , right max height)-h[i] for each index 

            We will create 2 arrays : left max and right max height 
            of size n for each index left and right heights '''
            

            