class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0 # left_index, right_index of the window
        min_window = "" # tracks the result
        diff = {} # difference in current window and t
        for char in t:
            diff[char] = diff.get(char, 0) + 1
        conflicts = len(diff) # number of characters conflicts

        while right < len(s):
            new_char = s[right]
            if new_char in diff:
                diff[new_char] -= 1
                if diff[new_char] == 0:
                    conflicts -= 1
            while conflicts == 0:
                curr_window = s[left:right + 1]
                if len(curr_window) < len(min_window) or min_window == "":
                    min_window = curr_window
                old_char = s[left]
                left += 1
                if old_char in diff:
                    diff[old_char] += 1
                    if diff[old_char] == 1:
                        conflicts += 1
            right += 1
        return min_window


