class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        diff = defaultdict(int)
        for char in s1:
            diff[char] += 1
        conflicts = len(diff)
        l, r = 0, 0
        while r < len(s2):
            new_char = s2[r]
            if new_char in diff:
                diff[new_char] -= 1
                if diff[new_char] == 0:
                    conflicts -= 1
            if r - l == len(s1):
                old_char = s2[l]
                l += 1
                if old_char in diff:
                    if diff[old_char] == 0:
                        conflicts += 1
                    diff[old_char] += 1
            if conflicts == 0:
                return True
            r += 1
        return False
