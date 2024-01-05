class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            # skip duplicate nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    # skip duplicate nums[j]
                    if j > i + 1 and nums[j] == nums[j - 1]:
                        pass
                    else:
                        res.append([nums[i], nums[j], nums[k]])
                    j += 1
        return res