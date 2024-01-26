class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_index, nums2_index, curr_index = m - 1, n - 1, m + n - 1 
        while nums2_index >= 0:
            if nums1_index >= 0:
                nums1_val = nums1[nums1_index] 
            nums2_val = nums2[nums2_index]
            if nums1_index >= 0 and nums1_val >= nums2_val:
                nums1[curr_index] = nums1_val
                curr_index -= 1
                nums1_index -=1 
            else:
                nums1[curr_index] = nums2_val
                curr_index -= 1
                nums2_index -= 1
        


        