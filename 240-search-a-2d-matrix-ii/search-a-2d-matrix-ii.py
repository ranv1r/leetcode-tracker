class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col, row = 0, len(matrix[0]) - 1
        while col < len(matrix) and row >= 0:
            print(col, row)
            current = matrix[col][row]
            if current == target:
                return True
            elif current > target:
                row -= 1
            else:
                col += 1
        return False
