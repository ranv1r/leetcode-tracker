class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        column = len(matrix[0]) - 1
        while column >= 0 and row < len(matrix):
            result = matrix[row][column]
            if result == target:
                return True
            elif result > target:
                column -= 1
            else:
                row += 1
        return False