class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            left, right = nums[l], nums[r]
            if left == right and l != r:
                r -= 1
                continue
            m = (l + r) // 2
            mid = nums[m]

            if mid == target:
                return True
            
            if left <= mid:
                if left <= target < mid:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if mid < target <= right:
                    l = m + 1
                else:
                    r = m - 1
        return False