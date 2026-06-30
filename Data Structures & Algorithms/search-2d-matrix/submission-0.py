class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''Since first integer in evrry row ,is greater than last integer
        of prev row ->
        first find optimal row using B Search and then ,
        find the target in that row using B search '''

        left,right=0,len(matrix)-1
        while left<=right:
            mid=(left+right)//2

            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]<target:
                left=mid+1
            else:
                right=mid-1

        #at the end of the loop 'right' will be at optimal location 
        left2=0 
        right2=len(matrix[0])-1

        while left2<=right2:
            mid=(left2+right2)//2

            if matrix[right][mid]==target:
                return True
            elif matrix[right][mid]<target:
                left2=mid+1
            else:
                right2=mid-1

        return False
        






