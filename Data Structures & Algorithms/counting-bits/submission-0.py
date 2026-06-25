class Solution:
    def countBits(self, n: int) -> List[int]:
        output=[]

        for i in range(0,n+1):
            res=0
            while i:
                res+=i & 1
                i >>= 1
            output.append(res)

        return output
            
