class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums=[-num for num in nums]
        heapq.heapify(nums)
        score,i=0,0
        while i<k:
            temp=heapq.heappop(nums)
            score=score-temp
            heapq.heappush(nums,temp//3)
            i+=1
        return score
