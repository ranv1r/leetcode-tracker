class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        d = deque([]) # monotonically decreasing queue (non-increasing) 
        while r < k:
            while d and d[-1] < nums[r]:
                d.pop()
            d.append(nums[r])
            r += 1
        res = [d[0]]
        while r < len(nums):
            while d and d[-1] < nums[r]:
                d.pop()
            d.append(nums[r])
            if d[0] == nums[l]:
                d.popleft()
            res.append(d[0])
            r += 1
            l += 1
        return res
