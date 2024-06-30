class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Calculate the counts
        counts = defaultdict(int)
        for x in nums:
            counts[x] += 1

        # Calculate the max count
        count_max = max(counts.values())

        # Rearrange into bucktes
        buckets = [[] for _ in range(count_max + 1)]
        for x, count in counts.items():
            buckets[count].append(x)

        # Iterate buckets in reverse order
        j = count_max # iteration index of buckets
        ret = []
        for _ in range(k):
            while len(buckets[j]) == 0:
                j -= 1
            ret.append(buckets[j].pop())
        return ret
            