class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        for i in nums:
            if i in unique_nums:
                return True
            unique_nums.add(i)
        return False