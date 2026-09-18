class Solution:
    def countBits(self, n: int) -> List[int]:
        output=[]

        for i in range(n+1):
            count=0
            num=i
            while num:
                num=num & (num-1)
                count+=1
            output.append(count)
        return output 
