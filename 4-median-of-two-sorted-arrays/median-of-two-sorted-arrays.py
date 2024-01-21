class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        m, n = len(A), len(B)
        l, r = 0, m - 1
        total = m + n
        half = total // 2

        while True:
            m1 = (l + r) // 2
            m2 = half - (m1 + 1) - 1

            leftA = A[m1] if m1 > -1 else float('-inf')
            leftB = B[m2] if m2 > -1 else float('-inf')
            rightA = A[m1 + 1] if m1 < m - 1 else float('inf')
            rightB = B[m2 + 1] if m2 < n - 1 else float('inf')

            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 1:
                    return min(rightA, rightB)
                else:
                    minRight = min(rightA, rightB)
                    maxLeft = max(leftA, leftB)
                    return (minRight + maxLeft) / 2
            elif leftA > rightB:
                r = m1 - 1
            else:
                l = m1 + 1 