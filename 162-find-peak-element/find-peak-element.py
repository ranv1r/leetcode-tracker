class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Search in direction which has the larger neighbor
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            mid = nums[m]
            left = nums[m - 1] if m - 1 >= 0 else float('-inf')
            right = nums[m + 1] if m + 1 < len(nums) else float('-inf')
            if mid > left and mid > right:
                return m
            elif left > mid:
                r = m - 1
            else:
                l = m + 1
        

