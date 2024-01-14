class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                total = nums[i] + nums[j] + nums[k]
                if total <= 0:
                    if total == 0:
                        res.append([nums[i], nums[j], nums[k]])
                    j += 1
                else:
                    k -= 1
        return res
