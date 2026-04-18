class MedianFinder:

    def __init__(self):
        self.minheap, self.maxheap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minheap, num)

        if self.maxheap and self.minheap[0] < -self.maxheap[0]:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)
        
        while len(self.maxheap) > len(self.minheap) + 1:
            val = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -val)

        while len(self.minheap) > len(self.maxheap) + 1:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2
        
        elif len(self.minheap) == len(self.maxheap) + 1:
            return self.minheap[0]

        elif len(self.maxheap) == len(self.minheap) + 1:
            return -self.maxheap[0]

        return





    # def __init__(self):
    #     self.minheap, self.maxheap = [], []       

    # def addNum(self, num: int) -> None:
    #     heapq.heappush(self.minheap, num)
    #     if self.maxheap and (-self.maxheap[0] > self.minheap[0]):
    #         var = heapq.heappop(self.minheap)
    #         heapq.heappush(self.maxheap, -var)
    #     while len(self.minheap) > len(self.maxheap) + 1:
    #         var = heapq.heappop(self.minheap)
    #         heapq.heappush(self.maxheap, -var)
    # def findMedian(self) -> float:
    #     if len(self.maxheap) == len(self.minheap):
    #         return (self.minheap[0] - self.maxheap[0]) / 2
    #     elif len(self.maxheap) > len(self.minheap):
    #         return -self.maxheap[0]
    #     elif len(self.minheap) > len(self.maxheap):
    #         return self.minheap[0]
    #     return 0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()