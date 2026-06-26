class Solution:
    def countBits(self, n: int) -> List[int]:
        '''We can notice its a series that repeats 
        at every 2's power it is 1 except 0 and at other places->
        eg-> for 5 -> no of 1's = no of 1's in 4 + no of 1's in 1'''
        
        output=[]
        memo={0:0}
        res=0
        for i in range(0,n+1):
            '''Normally calculating every number bits from scratch
            takes lot of time we can save results that occur
            multiple times-> DP memoization'''

            res+=self.recbits(i,memo)
            output.append(res)
            res=0

        return output

    def recbits(self,n,memo):
        if n in memo:
            return memo[n]
        elif n > 0 and (n & (n - 1)) == 0:
            '''THe above is a confirm check if a no is power of 2'''
            memo[n]=1
            return 1
        else:
            memo[n]=self.recbits(n//2,memo)+self.recbits(n%2,memo)
            return memo[n]
        