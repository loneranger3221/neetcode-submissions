class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1,p2=0,len(numbers)-1
        while p1<p2:
            nsum=numbers[p1]+numbers[p2]
            if nsum>target:
                p2-=1
            elif nsum<target:
                p1+=1
            else:
                return [p1+1,p2+1]



        