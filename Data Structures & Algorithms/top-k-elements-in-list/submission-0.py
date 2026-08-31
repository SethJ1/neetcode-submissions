class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        sorted_counts = sorted(
            counts.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [x[0] for x in sorted_counts[:k]]