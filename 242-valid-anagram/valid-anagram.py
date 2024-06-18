class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(int)
        for i in s:
            counts[i] += 1
        for i in t:
            counts[i] -= 1
        for i, x in counts.items():
            if x != 0:
                return False
        return True