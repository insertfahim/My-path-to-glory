class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns=len(matrix[0])
        top = 0
        bottom=rows-1
        while top<=bottom:
            row = (top+bottom)//2
            if target<matrix[row][0]:
                bottom=row-1
            elif target>matrix[row][-1]:
                top=row+1
            else:
                break
        left,right = 0,columns-1
        while left<=right:
            mid = (left+right)//2
            mid_value = matrix[row][mid]
            if mid_value>target:
                right=mid-1
            elif mid_value<target:
                left=mid+1
            else:
                return True
        return False