class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        ans=0
        remainingCapacity=[cap-rock for cap , rock in zip(capacity,rocks)]
        remainingCapacity.sort()
        for val in remainingCapacity:
            if val<=additionalRocks:
                additionalRocks-=val
                ans+=1
            else:
                break
        return ans
