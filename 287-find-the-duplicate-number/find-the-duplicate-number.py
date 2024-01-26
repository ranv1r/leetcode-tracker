class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while slow != fast or slow == 0:
            slow, fast = nums[slow], nums[nums[fast]]
        slow1 = 0 # slow pointer from start
        slow2 = slow # slow pointer from meeting point
        # these pointers will meet at tne entracne of the cycle
        # that is the duplicate number 
        while slow1 != slow2:
            slow1 = nums[slow1]
            slow2 = nums[slow2]
        return slow1