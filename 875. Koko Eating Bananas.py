class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        def check(speed):
            time=0
            for pile in piles:
                time+=(speed+pile-1)//speed
            return time<=h
        while left<right:
            mid=(left+right)//2
            if check(mid):
                right=mid
            else:
                left=mid+1
        return left
