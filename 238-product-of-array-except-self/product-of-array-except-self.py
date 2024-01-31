class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [] # store right product in res
        
        # first pass: calculate right product and store in res
        right_product = 1
        for x in reversed(nums):
            res.append(right_product)
            right_product *= x

        res.reverse()

        left_product = 1
        # calculate left product ont the fly using left_product variable
        for i in range(len(nums)):
            res[i] = res[i] * left_product
            left_product *= nums[i]
        return res