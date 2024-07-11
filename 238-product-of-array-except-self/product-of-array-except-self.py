class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        # adding right product to output in a reversed way
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            output.append(right_product)
            right_product = right_product * nums[i]

        # reversing output
        for i in range(len(nums) // 2):
            output[i], output[len(nums) - 1 - i] = output[len(nums) - 1 - i], output[i]
        

        # adding left product to output
        left_product = 1
        for i in range(len(nums)):
            output[i] = left_product * output[i]
            left_product = left_product * nums[i]

        return output        
