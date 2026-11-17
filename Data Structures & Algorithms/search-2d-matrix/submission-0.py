class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)  # number of rows
        n = len(matrix[0])  # number of columns
        row = []

        left = 0
        right = m-1

        while left <= right:
            mid = (left + right) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][n-1]:
                row = matrix[mid]
                break
            elif target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][n-1]:
                left = mid + 1

        if not row:
            return False

        left = 0  
        right = n-1

        while left <= right:
            mid = (left + right) // 2

            if target == row[mid]:
                return True
            elif target < row[mid]:
                right = mid - 1
            elif target > row[mid]:
                left = mid + 1

        return False
