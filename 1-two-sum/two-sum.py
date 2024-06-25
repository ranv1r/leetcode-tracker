class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # index the number and the difference from target
        diffs = {}
        for i, x in enumerate(nums):
            if x in diffs:
                return [i, diffs[x]]
            else:
                diffs[target - x] = i
