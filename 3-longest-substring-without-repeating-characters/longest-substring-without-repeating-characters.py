class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        last_index = {}
        result = 0
        while r < len(s): 
            new = s[r]

            if new in last_index:
                index = last_index[new]
                while l <= index:
                    del last_index[s[l]]
                    l += 1
                l = index + 1

            last_index[new] = r
            result = max(result, r - l + 1)
            r += 1
        return result



