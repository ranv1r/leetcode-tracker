class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(matrix):
            # last element of row
            j = matrix[i][-1]
            if j == target:
                return True
            if j > target:
                result = self.binarySearch(matrix[i], target)
                if result:
                    return True
            i += 1
    
    def binarySearch(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False