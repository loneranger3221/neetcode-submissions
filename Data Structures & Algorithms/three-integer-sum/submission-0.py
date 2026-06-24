class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''We will try to solve this problem in parts 
        i.e first sort the array to ensure no duplicates are being used,
        then for a first number , use two sum II for the rest to find the 
        other half for which total sum becomes 0'''


        sortnum=sorted(nums)
        res=[]
        for i in range(0,len(sortnum)):
            if i>0 and sortnum[i]!=sortnum[i-1] or i==0:
                a=sortnum[i]
            else:
                continue
            '''Using TWO SUM II concept for sorted array for the rest'''
            p1,p2=i+1,len(sortnum)-1
            target=0-a
            while p1<p2:
                sum=sortnum[p1]+sortnum[p2]
                if sum>target:
                    p2-=1
                elif sum<target:
                    p1+=1
                else:
                    res.append([a,sortnum[p1],sortnum[p2]])
                    p1+=1
                    p2-=1

                    while p1 < p2 and sortnum[p1] == sortnum[p1 - 1]:
                        p1 += 1
        
        return res 

            


