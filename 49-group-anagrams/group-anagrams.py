class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)
        for string in strs:
            counts = [0 for _ in range(26)] # one zero for every letter
            for ch in string:
                i = self.letter_index(ch) 
                counts[i] = counts[i] + 1  
            buckets[tuple(counts)].append(string)
        return list(buckets.values())

    def letter_index(self, letter: str) -> int:
        return ord(letter) - ord('a')
