class Solution:
    ''' 1st Approach -> GAVE TLE 
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 1 if nums[0]==k else 0
        count=0
        for comb in range(1,len(nums)):
            sum=0
            for i in range(comb):
                sum+=nums[i]
            for i in range(comb,len(nums)):
                if sum==k:
                    count+=1
                sum+=nums[i]-nums[i-comb]
            if sum==k:
                count+=1
        return count''' 

    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        current_sum = 0
        
        # Dictionary to store { prefix_sum : frequency }
        # Initialize with 0:1 to catch subarrays that start at index 0
        prefix_sums = {0: 1}
        
        for num in nums:
            current_sum += num
            
            # Check if there's a prefix sum we can subtract to get 'k'
            target = current_sum - k
            if target in prefix_sums:
                count += prefix_sums[target]
                
            # Add the current sum to our dictionary (or update its frequency)
            if current_sum in prefix_sums:
                prefix_sums[current_sum] += 1
            else:
                prefix_sums[current_sum] = 1
                
        return count











    