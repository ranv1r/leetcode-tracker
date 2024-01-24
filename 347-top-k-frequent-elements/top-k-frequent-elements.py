class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for x in nums:
            counts[x] += 1
        buckets = defaultdict(list)
        for x, count in counts.items():
            buckets[count].append(x)
        res = []
        i = len(nums)
        while len(res) != k:
            if buckets[i]:
                res.extend(buckets[i])
            i -= 1
        return res