class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''THis is sliding window so two pointers next to each other
        maintainig a variable/fixed sized window'''
        
        if len(prices)==1 or not prices :
            return 0

        maxprof=0
        left=0 #buy pointer"
        right=1 #sell pointer"

        while right<len(prices):
            prof=prices[right]-prices[left]
            if prof<0:
                '''It means buying price more than selling price 
                so we make selling prie as new buying price'''
                left=right
            else:
                '''Means profit is positive, store the max profit'''
                maxprof=max(maxprof,prof)

            right+=1 #always move sell pointer forward
            
        return maxprof


