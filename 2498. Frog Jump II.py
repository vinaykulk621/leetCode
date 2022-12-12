class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n=len(stones)
        if n==2:
            return stones[-1]
        min_cost=-1
        for i in range(n-2):
            min_cost=max(min_cost,stones[i+2]-stones[i])
        return min_cost
