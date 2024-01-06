class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # binary searching the partition on the smaller array
        small, large = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        m, n = len(small), len(large)
        half = (m + n) // 2
        left, right = 0, m

        while True:
            mid_small = left + ((right - left) // 2)
            mid_large = half - mid_small

            small_partition_left = small[mid_small - 1] if mid_small - 1 >= 0 else float('-inf')
            large_partition_left = large[mid_large - 1] if mid_large - 1 >= 0 else float('-inf')
            small_partition_right = small[mid_small] if mid_small < len(small) else float('inf')
            large_partition_right = large[mid_large] if mid_large < len(large) else float('inf')

            if small_partition_left <= large_partition_right and large_partition_left <= small_partition_right:
                if ((m + n) % 2) == 0:
                    median_left = max(small_partition_left, large_partition_left)
                    median_right = min(small_partition_right, large_partition_right)
                    return (median_left + median_right) / 2
                else:
                    return min(small_partition_right, large_partition_right)
            elif small_partition_left > large_partition_right:
                right = mid_small - 1
            else:
                left = mid_small + 1