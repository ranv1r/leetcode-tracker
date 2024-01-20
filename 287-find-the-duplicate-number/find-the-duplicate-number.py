class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        slow, cycle = slow, 0
        while True:
            slow, cycle = nums[slow], nums[cycle]
            if slow == cycle:
                return cycle
        