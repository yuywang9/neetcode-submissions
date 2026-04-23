class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap1 = []
        for num, counter in freq.items():
            heapq.heappush(heap1, (counter, num))

            while len(heap1) > k:
                heapq.heappop(heap1)
            
        res = []
        for counter, num in heap1:
            res.append(num)
        return res