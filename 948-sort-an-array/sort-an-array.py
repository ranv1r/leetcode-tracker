class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        h = len(nums) // 2
        l = self.sortArray(nums[:h])
        r = self.sortArray(nums[h:])
        return self.mergeTwoLists(l, r)
    
    def mergeTwoLists(self, nums1, nums2):
        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        if i < len(nums1):
            result.extend(nums1[i:])
        if j < len(nums2):
            result.extend(nums2[j:])
        return result