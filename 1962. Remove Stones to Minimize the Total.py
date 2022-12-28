import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles=[-rock for rock in piles]
        heapq.heapify(piles)
        for _ in range(k):
            sub=-heapq.heappop(piles)
            heapq.heappush(piles,-(sub-sub//2))
            k-=1
        return -sum(piles)
