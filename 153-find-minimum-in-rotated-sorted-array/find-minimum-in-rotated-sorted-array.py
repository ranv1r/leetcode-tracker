class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            m = (l + r) // 2
            left, right, mid = nums[l], nums[r], nums[m]

            if left <= right:
                res = min(res, mid)
                r = m - 1
            else:
                if mid >= left:
                    l = m + 1
                else:
                    res = min(res, mid)
                    r = m - 1
                
        return res


                